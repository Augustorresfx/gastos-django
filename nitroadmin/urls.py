"""nitroadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clients import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('gastos/', views.gastos, name='gastos'),
    path('gastos/create/', views.create_gasto, name="crear_gasto"),
    path('gastos/<int:product_id>/', views.gasto_detail, name='gasto_detail'),
    path('gastos/<int:product_id>/delete/', views.delete_client, name='delete_gasto'),
    path('gastos/export_excel', views.export_excel, name="export_excel"),
    path('expensas/', views.expensas, name='expensas'),
    path('expensas/create/', views.create_expensa, name="crear_expensa"),
    path('expensas/<int:gasto_id>/', views.expensa_detail, name='expensa_detail'),
    path('expensas/<int:gasto_id>/delete/', views.delete_expensa, name='delete_expensa'),
    path('logout/', views.signout, name='logout'),
    path('search-expenses', csrf_exempt(views.search_expenses),
         name="search_expenses"),
    path('signin/', views.signin, name='signin')
]
