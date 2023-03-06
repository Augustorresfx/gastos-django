from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ClientForm, ClientFilterForm, GastoForm
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .filters import ProductFilter
import csv
from django.http import HttpResponse
import xlwt
from datetime import timedelta, datetime
from django.http import JsonResponse
import json
import openpyxl
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Alignment,Border,Font,PatternFill,Side
import pandas as pd
from .models import Gasto

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
        expenses = Product.objects.filter(
            price__istartswith=search_str, ) | Product.objects.filter(
            created__istartswith=search_str, ) | Product.objects.filter(
            description__icontains=search_str, ) | Product.objects.filter(
            category__icontains=search_str, )
        data = expenses.values()
        return JsonResponse(list(data), safe=False)

@login_required
def gastos(request):
  
    context = {}   

    filtered_clients = ProductFilter(
        request.GET, 
        queryset=Product.objects.all()
        )
    context['clients'] = filtered_clients.qs
    paginated_filter = Paginator(filtered_clients.qs, 3)
    page_number = request.GET.get("page")
    filter_pages = paginated_filter.get_page(page_number)
   
    context['form'] = filtered_clients.form
    context['pages'] = filter_pages
    categories = Category.objects.all()
   
    return render(request, 'gastos.html', context=context)

@login_required
def expensas(request):
  
    context = {}   


    context['clients'] = Gasto.objects.all()
    paginated_filter = Paginator(Gasto.objects.all(), 3)
    page_number = request.GET.get("page")
    filter_pages = paginated_filter.get_page(page_number)
   

    context['pages'] = filter_pages
    categories = Category.objects.all()
   
    return render(request, 'expensas.html', context=context)

@login_required
def create_expensa(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'create_expensa.html', {
            'form': GastoForm,
            'categories': categories,
        })
    else:
        try:
            
            form = GastoForm(request.POST)
            new_client = form.save(commit=False)
            new_client.save()
            return redirect('expensas')
        except ValueError:
            return render(request, 'create_expensa.html', {
                'form': GastoForm,
                'error': 'Please provide valid data'
            })

@login_required
def create_gasto(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'create_gasto.html', {
            'form': ClientForm,
            'categories': categories,
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
            return render(request, 'expensa_detail.html', {'expensa': gasto, 'form': form, 'error': 'Error actualizando el cliente'})


@login_required
def delete_expensa(request, gasto_id):
    gasto = get_object_or_404(Gasto, pk=gasto_id)
    if request.method == 'POST':
        gasto.delete()
        return redirect('expensas')


@login_required
def gasto_detail(request, product_id):
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=product_id, user=request.user)
        form = ClientForm(instance=product)
        return render(request, 'gasto_detail.html', {'client': product, 'form': form})
    else:
        try:
            product = get_object_or_404(Product, pk=product_id)
            form = ClientForm(request.POST, instance=product)
            form.save()
            return redirect('gastos')
        except ValueError:
            return render(request, 'gastos_detail.html', {'client': product, 'form': form, 'error': 'Error actualizando el cliente'})


@login_required
def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Reporte_Diario' + \
        str(datetime.now())+'.xlsx'
    path = "C:\\Users\\augus\\Downloads\\backend-python-master\\backend-python-master\\clients\\excel\\Reporte_diario.xlsx"
    wb = load_workbook(path)
    wb.iso_dates = True
    sheet = wb.active
    max_col = sheet.max_column

    
    products = Product.objects.all()   
    

    for product in products:
        timeformat = "%H:%M:%S"
        delta = datetime.strptime(str(product.landing_time), timeformat) - datetime.strptime(str(product.takeoff_time), timeformat)
        
        data = [product.takeoff_place, product.created.strftime("%d %m %y"), '', product.pilot.name, product.mechanic.name, product.operator.name, product.category.title, timedelta(seconds=delta.seconds), '', product.reason_of_flight.title, '', '', '', product.start_up_cycles, '', '', '', '', '', product.price, '', '', '', '', product.engine_ignition_1, product.engine_cut_1, product.engine_ignition_2, product.engine_cut_2]
    
        sheet.append(data)

    wb.save(response)  

    return response


@login_required
def delete_client(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('gastos')

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