from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ClientForm, ClientFilterForm
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .filters import ProductFilter
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
                return redirect('clients')           
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

@login_required
def clients(request):
  
    context = {}   

    filtered_clients = ProductFilter(
        request.GET, 
        queryset=Product.objects.all()
        )
    context['clients'] = filtered_clients.qs
    paginated_filter = Paginator(filtered_clients.qs, 1)
    page_number = request.GET.get("page")
    filter_pages = paginated_filter.get_page(page_number)
   
    context['form'] = filtered_clients.form
    context['pages'] = filter_pages
    categories = Category.objects.all()
   
    return render(request, 'clients.html', context=context)

@login_required
def create_product(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'create_product.html', {
            'form': ClientForm,
            'categories': categories,
        })
    else:
        try:
            
            form = ClientForm(request.POST)
            print(form)
            new_client = form.save(commit=False)
            new_client.user = request.user
            new_client.save()
            return redirect('clients')
        except ValueError:
            return render(request, 'create_product.html', {
                'form': ClientForm,
                'error': 'Please provide valid data'
            })

@login_required
def client_detail(request, product_id):
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=product_id, user=request.user)
        form = ClientForm(instance=product)
        return render(request, 'client_detail.html', {'client': product, 'form': form})
    else:
        try:
            product = get_object_or_404(Product, pk=product_id)
            form = ClientForm(request.POST, instance=product)
            form.save()
            return redirect('clients')
        except ValueError:
            return render(request, 'client_detail.html', {'client': product, 'form': form, 'error': 'Error actualizando el cliente'})

@login_required
def delete_client(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('clients')

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
            return redirect('clients')