from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ClientForm, ClientFilterForm, GastoForm, AeronaveForm, PilotoForm, MecanicoForm
from .models import Operacion, Aeronave, Impuesto, Mecanico, Piloto
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .filters import ProductFilter
from django.http import HttpResponse
import xlwt
from datetime import timedelta, datetime, date, time
from django.http import JsonResponse
import json
import openpyxl
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Alignment,Border,Font,PatternFill,Side
from .models import Gasto
import os
from io import BytesIO
import smtplib
from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders

from dotenv import load_dotenv
from django.utils.formats import date_format
from django.utils.dateparse import parse_date
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy

def is_staff_user(user):
    return user.is_staff

staff_required = user_passes_test(is_staff_user, login_url=reverse_lazy('signin'))


def is_basic_user(user):
    return user.groups.filter(name='PermisoBasico').exists()
load_dotenv()
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
              
                user = User.objects.create_user(username=request.POST['username'], 
                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('gastos')           
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })
        else:
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'Las constraseñas no coinciden'
            })

def search_expenses(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        expenses = Operacion.objects.filter(
            price__istartswith=search_str, ) | Operacion.objects.filter(
            created__istartswith=search_str, ) | Operacion.objects.filter(
            description__icontains=search_str, ) | Operacion.objects.filter(
            category__icontains=search_str, )
        data = expenses.values()
        return JsonResponse(list(data), safe=False)

@login_required
@user_passes_test(lambda user: user.groups.filter(name='PermisoBasico').exists() or user.is_staff)

def gastos(request):
  
    context = {}   
    
    filtered_clients = ProductFilter(
        request.GET, 
        queryset=Operacion.objects.all(),

        )

    context['clients'] = filtered_clients.qs
    paginated_filter = Paginator(filtered_clients.qs, 10)
    page_number = request.GET.get("page")
    filter_pages = paginated_filter.get_page(page_number)
   
    context['form'] = filtered_clients.form
    context['pages'] = filter_pages
    
    return render(request, 'gastos.html', context=context)

@login_required
@user_passes_test(lambda user: user.groups.filter(name='PermisoBasico').exists() or user.is_staff)

def expensas(request):
  
    context = {}   
    context['clients'] = Gasto.objects.all()
    paginated_filter = Paginator(Gasto.objects.all(), 3)
    page_number = request.GET.get("page")
    filter_pages = paginated_filter.get_page(page_number)
    context['pages'] = filter_pages
   
    return render(request, 'expensas.html', context=context)

@login_required
@user_passes_test(lambda user: user.groups.filter(name='PermisoBasico').exists() or user.is_staff)

def create_expensa(request):
    if request.method == 'GET':

        return render(request, 'create_expensa.html', {
            'form': GastoForm,
        })
    else:
        try:
            
            form = GastoForm(request.POST)
            new_client = form.save(commit=False)
            new_client.user = request.user
            new_client.save()
            return redirect('expensas')
        except ValueError:
            return render(request, 'create_expensa.html', {
                'form': GastoForm,
                'error': 'Please provide valid data'
            })

@login_required
@user_passes_test(lambda user: user.groups.filter(name='PermisoBasico').exists() or user.is_staff)

def create_gasto(request):
    if request.method == 'GET':

        return render(request, 'create_gasto.html', {
            'form': ClientForm,

        })
    else:
        try:
            
            form = ClientForm(request.POST)
            new_client = form.save(commit=False)
            new_client.user = request.user
            new_client.save()
            return redirect('gastos')
        except ValueError:
            return render(request, 'create_gasto.html', {
                'form': ClientForm,
                'error': 'Please provide valid data'
            })

@login_required
@user_passes_test(lambda user: user.groups.filter(name='PermisoBasico').exists() or user.is_staff)

def expensa_detail(request, gasto_id):
    if request.method == 'GET':
        gasto = get_object_or_404(Gasto, pk=gasto_id)
        form = GastoForm(instance=gasto)
        return render(request, 'expensa_detail.html', {'expensa': gasto, 'form': form})
    else:
        try:
            gasto = get_object_or_404(Gasto, pk=gasto_id)
            form = GastoForm(request.POST, instance=gasto)
            form.save()
            return redirect('expensas')
        except ValueError:
            return render(request, 'expensa_detail.html', {'expensa': gasto, 'form': form, 'error': 'Error actualizando el gasto'})


@login_required
@user_passes_test(lambda user: user.groups.filter(name='PermisoBasico').exists() or user.is_staff)

# def delete_expensa(request, gasto_id):
#     gasto = get_object_or_404(Gasto, pk=gasto_id)
#     if request.method == 'POST':
#         gasto.delete()
#         return redirect('expensas')

def delete_expensa(request, gasto_id):
    gasto = get_object_or_404(Gasto, pk=gasto_id)
    if gasto.user == request.user or request.user.is_staff:
        if request.method == 'POST':
            gasto.delete()
            messages.success(request, 'Elemento eliminado correctamente')
            return redirect('expensas')
        else:
            return render(request, 'delete_expensa.html', {'gasto': gasto})
    else:
        messages.error(request, 'No tienes permiso para eliminar este elemento')
        return redirect('expensas')

@login_required
@user_passes_test(lambda user: user.groups.filter(name='PermisoBasico').exists() or user.is_staff)

def gasto_detail(request, product_id):
    if request.method == 'GET':
        product = get_object_or_404(Operacion, pk=product_id, user=request.user)
        form = ClientForm(instance=product)
        return render(request, 'gasto_detail.html', {'client': product, 'form': form})
    else:
        try:
            product = get_object_or_404(Operacion, pk=product_id)
            form = ClientForm(request.POST, instance=product)
            form.save()
            return redirect('gastos')
        except ValueError:
            return render(request, 'gasto_detail.html', {'client': product, 'form': form, 'error': 'Error actualizando la operación'})

def send_mail_with_excel(request):
    module_dir = os.path.dirname(__file__)   #get current directory
    file_path = os.path.join(module_dir, 'static/Reporte_diario.xlsx')   #full path to text.
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Reporte_Diario ' + \
    str(timezone.now().date())+'.xlsx'
    path = file_path
    wb = load_workbook(path)
    wb.iso_dates = True
    sheet = wb.active
    max_col = sheet.max_column

    # Obtener fecha y hora actual en la zona horaria del proyecto
    hoy = timezone.now().date()  # Obtiene la fecha actual
    objetos_hoy = Operacion.objects.filter(created__date=hoy)

    objetos_todos = Operacion.objects.all()

    row = 9  # empezar a agregar en la fila 6
    col = 1  # agregar en la primera columna
    for product in objetos_todos:
        timeformat = "%H:%M:%S"
        delta = datetime.strptime(str(product.landing_time), timeformat) - datetime.strptime(str(product.takeoff_time), timeformat)
        combustible_usado = product.fuel - product.fuel_on_landing
        data = [product.takeoff_place, product.created.strftime("%y %m %d"), '', product.pilot.name, product.mechanic.name, product.operator.name, product.aeronave.title, timedelta(seconds=delta.seconds), '', product.reason_of_flight.title, '', '', '', product.start_up_cycles, '', '', '', product.fuel, product.fuel_on_landing, combustible_usado, product.engine_ignition_1, product.engine_cut_1, product.total_encendido_1, product.engine_ignition_2, product.engine_cut_2, product.total_encendido_2, product.operation_note, product.maintenance_note, product.client.name, product.cycles_with_external_load, product.weight_with_external_load, product.number_of_landings, product.number_of_splashdowns, product.water_release_cycles, product.water_release_amount]
        
        for i, val in enumerate(data):
            sheet.cell(row=row, column=col+i, value=val)
        row+=1

    excel_file = BytesIO()
    wb.save(excel_file)
    excel_file.seek(0)
    destinatarios = ['gguerra@helicopterosdelpacifico.com.ar', 'augustorresfx@gmail.com', 'agustorres633@gmail.com']

    try:
        for destinatario in destinatarios:

            msg = MIMEMultipart()
            msg['From'] = 'no.reply.wings@gmail.com'
            msg['To'] = destinatario

            msg['Subject'] = 'Su reporte del día'

            part = MIMEBase('application', 'octet-stream')
            part.set_payload((excel_file).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename='Reporte_Diario' + \
            str(datetime.now())+'.xlsx')
            msg.attach(part)

            html = """\
                <html>
                <head></head>
                <body>
                    <h1>Estimado/a,</h1>
                    <h2>Adjunto encontrará el archivo de Excel con los datos solicitados:</h2>
                </body>
                </html>
                """
            msg.attach(MIMEText(html, 'html'))

            # Conectar y enviar el correo electrónico
            smtp_server = 'smtp.gmail.com'  # Cambia esto a tu servidor SMTP
            smtp_port = 587  # Cambia esto al puerto de tu servidor SMTP
            smtp_user = os.getenv('SMTP_USER')
            smtp_password = os.getenv('SMTP_PASSWORD')  # Cambia esto a tu contraseña SMTP
            smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
            smtp_connection.starttls()
            smtp_connection.login(smtp_user, smtp_password)
            smtp_connection.sendmail(smtp_user, msg['To'], msg.as_string())
            smtp_connection.quit()
            excel_file.seek(0)
        messages.success(request, 'Los correos electrónicos se enviaron correctamente')
    except:
        messages.error(request, 'Error enviando los correos electrónicos')
    
    
    return redirect('gastos')

@login_required
def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Reporte_Diario ' + \
        str(timezone.now().date())+'.xlsx'
    module_dir = os.path.dirname(__file__)   #get current directory
    file_path = os.path.join(module_dir, 'static/Reporte_diario.xlsx')   #full path to text.
    path = file_path
    wb = load_workbook(path)
    wb.iso_dates = True
    sheet = wb.active
    max_col = sheet.max_column

    
    hoy = timezone.now().date()  # Obtiene la fecha actual
    objetos_hoy = Operacion.objects.filter(created__date=hoy)

    objetos_todos = Operacion.objects.all()

    row = 9  # empezar a agregar en la fila 6
    col = 1  # agregar en la primera columna
    for product in objetos_todos:
        timeformat = "%H:%M:%S"
        delta = datetime.strptime(str(product.landing_time), timeformat) - datetime.strptime(str(product.takeoff_time), timeformat)

        data = [product.takeoff_place, product.created.strftime("%y %m %d"), '', product.pilot.name, product.mechanic.name, product.operator.name, product.aeronave.title, timedelta(seconds=delta.seconds), '', product.reason_of_flight.title, '', '', '', product.start_up_cycles, '', '', '', product.fuel, product.fuel_on_landing, product.used_fuel, product.engine_ignition_1, product.engine_cut_1, product.engine_ignition_2, product.engine_cut_2, product.operation_note, product.maintenance_note, product.client.name, product.cycles_with_external_load, product.weight_with_external_load, product.number_of_landings, product.number_of_splashdowns, product.water_release_cycles, product.water_release_amount]

        for i, val in enumerate(data):
            sheet.cell(row=row, column=col+i, value=val)
        row+=1


    wb.save(response)  

    return response

@login_required
@user_passes_test(lambda user: user.groups.filter(name='PermisoBasico').exists() or user.is_staff)
# def delete_gasto(request, product_id):
#     product = get_object_or_404(Operacion, pk=product_id)
#     if request.method == 'POST':
#         product.delete()
#         return redirect('gastos')


def delete_gasto(request, product_id):
    product = get_object_or_404(Operacion, pk=product_id)
    if product.user == request.user or request.user.is_staff:
        if request.method == 'POST':
            product.delete()
            messages.success(request, 'Elemento eliminado correctamente')
            return redirect('gastos')
        else:
            return render(request, 'delete_gasto.html', {'product': product})
    else:
        messages.error(request, 'No tienes permiso para eliminar este elemento')
        return redirect('gastos')

#  AERONAVES

@login_required
@staff_required
def aeronaves(request):

    context = {}   
    context['aeronaves'] = Aeronave.objects.all()
    paginated_filter = Paginator(Aeronave.objects.all(), 10)
    page_number = request.GET.get("page")
    filter_pages = paginated_filter.get_page(page_number)
    context['pages'] = filter_pages
   
    return render(request, 'aeronaves.html', context=context)

@login_required
@staff_required

def create_aeronave(request):
    if request.method == 'GET':

        return render(request, 'create_aeronave.html', {
            'form': AeronaveForm,

        })
    else:
        try:
            
            form = AeronaveForm(request.POST)
            new_client = form.save(commit=False)
            new_client.user = request.user
            new_client.save()
            return redirect('aeronaves')
        except ValueError:
            return render(request, 'create_aeronave.html', {
                'form': AeronaveForm,
                'error': 'Please provide valid data'
            })

@login_required
@staff_required

def aeronave_detail(request, aeronave_id):
    if request.method == 'GET':
        aeronave = get_object_or_404(Aeronave, pk=aeronave_id)
        form = AeronaveForm(instance=aeronave)
        return render(request, 'aeronave_detail.html', {'aeronave': aeronave, 'form': form})
    else:
        try:
            aeronave = get_object_or_404(Aeronave, pk=aeronave_id)
            form = AeronaveForm(request.POST, instance=aeronave)
            form.save()
            return redirect('aeronaves')
        except ValueError:
            return render(request, 'aeronave_detail.html', {'aeronave': aeronave, 'form': form, 'error': 'Error actualizando la aeronave'})


@login_required
@staff_required

def delete_aeronave(request, aeronave_id):
    aeronave = get_object_or_404(Aeronave, pk=aeronave_id)
    if request.method == 'POST':
        aeronave.delete()
        return redirect('aeronaves')

# FIN AERONAVES

# PILOTOS

@login_required
@staff_required

def pilotos(request):
  
    context = {}   
    context['pilotos'] = Piloto.objects.all()
    paginated_filter = Paginator(Aeronave.objects.all(), 10)
    page_number = request.GET.get("page")
    filter_pages = paginated_filter.get_page(page_number)
    context['pages'] = filter_pages
   
    return render(request, 'pilotos.html', context=context)

@login_required
@staff_required

def create_piloto(request):
    if request.method == 'GET':

        return render(request, 'create_piloto.html', {
            'form': PilotoForm,

        })
    else:
        try:
            
            form = PilotoForm(request.POST)
            new_client = form.save(commit=False)
            new_client.user = request.user
            new_client.save()
            return redirect('pilotos')
        except ValueError:
            return render(request, 'create_piloto.html', {
                'form': PilotoForm,
                'error': 'Please provide valid data'
            })

@login_required
@staff_required

def piloto_detail(request, piloto_id):
    if request.method == 'GET':
        piloto = get_object_or_404(Piloto, pk=piloto_id)
        form = PilotoForm(instance=piloto)
        return render(request, 'piloto_detail.html', {'piloto': piloto, 'form': form})
    else:
        try:
            piloto = get_object_or_404(Piloto, pk=piloto_id)
            form = PilotoForm(request.POST, instance=piloto)
            form.save()
            return redirect('pilotos')
        except ValueError:
            return render(request, 'piloto_detail.html', {'piloto': piloto, 'form': form, 'error': 'Error actualizando la aeronave'})


@login_required
@staff_required

def delete_piloto(request, piloto_id):
    piloto = get_object_or_404(Piloto, pk=piloto_id)
    if request.method == 'POST':
        piloto.delete()
        return redirect('pilotos')

# FIN PILOTOS

# MECANICOS

@login_required
@staff_required

def mecanicos(request):
  
    context = {}   
    context['mecanicos'] = Mecanico.objects.all()
    paginated_filter = Paginator(Aeronave.objects.all(), 10)
    page_number = request.GET.get("page")
    filter_pages = paginated_filter.get_page(page_number)
    context['pages'] = filter_pages
   
    return render(request, 'mecanicos.html', context=context)

@login_required
@staff_required

def create_mecanico(request):
    if request.method == 'GET':

        return render(request, 'create_mecanico.html', {
            'form': MecanicoForm,

        })
    else:
        try:
            
            form = MecanicoForm(request.POST)
            new_client = form.save(commit=False)
            new_client.user = request.user
            new_client.save()
            return redirect('mecanicos')
        except ValueError:
            return render(request, 'create_mecanico.html', {
                'form': MecanicoForm,
                'error': 'Please provide valid data'
            })

@login_required
@staff_required

def mecanico_detail(request, mecanico_id):
    if request.method == 'GET':
        mecanico = get_object_or_404(Mecanico, pk=mecanico_id)
        form = MecanicoForm(instance=mecanico)
        return render(request, 'mecanico_detail.html', {'mecanico': mecanico, 'form': form})
    else:
        try:
            mecanico = get_object_or_404(Mecanico, pk=mecanico_id)
            form = MecanicoForm(request.POST, instance=mecanico)
            form.save()
            return redirect('mecanicos')
        except ValueError:
            return render(request, 'mecanico_detail.html', {'mecanico': mecanico, 'form': form, 'error': 'Error actualizando la aeronave'})


@login_required
@staff_required

def delete_mecanico(request, mecanico_id):
    mecanico = get_object_or_404(Mecanico, pk=mecanico_id)
    if request.method == 'POST':
        mecanico.delete()
        return redirect('mecanicos')

# FIN MECANICOS
@login_required

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], 
            password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'El nombre de usuario o la contraseña no existen',
            })
        else:
            login(request, user)
            return redirect('gastos')