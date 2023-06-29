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
    path('pilotos/', views.pilotos, name='pilotos'),
    path('pilotos/create/', views.create_piloto, name='crear_piloto'),
    path('pilotos/<int:piloto_id>/', views.piloto_detail, name='piloto_detail'),
    path('pilotos/<int:piloto_id>/delete/', views.delete_piloto, name='delete_piloto'),
    path('otros/', views.otros, name='otros'),
    path('otros/create/', views.create_otro, name='crear_otro'),
    path('otros/<int:otro_id>/', views.otro_detail, name='otro_detail'),
    path('otros/<int:otro_id>/delete/', views.delete_otro, name='delete_otro'),
    path('mecanicos/', views.mecanicos, name='mecanicos'),
    path('mecanicos/create/', views.create_mecanico, name='crear_mecanico'),
    path('mecanicos/<int:mecanico_id>/', views.mecanico_detail, name='mecanico_detail'),
    path('mecanicos/<int:mecanico_id>/delete/', views.delete_mecanico, name='delete_mecanico'),
    path('aeronaves/', views.aeronaves, name='aeronaves'),
    path('aeronaves/create/', views.create_aeronave, name='crear_aeronave'),
    path('aeronaves/<int:aeronave_id>/', views.aeronave_detail, name='aeronave_detail'),
    path('aeronaves/<int:aeronave_id>/delete/', views.delete_aeronave, name='delete_aeronave'),
    path('vuelos/', views.vuelos, name='vuelos'),
    path('vuelos/create/', views.create_vuelo, name="crear_vuelo"),
    path('vuelos/<int:product_id>/', views.vuelo_detail, name='vuelo_detail'),
    path('vuelos/<int:product_id>/delete/', views.delete_vuelo, name='delete_vuelo'),
    path('vuelos/export_excel', views.export_excel, name="export_excel"),
    path('vuelos/export_excel_gmail', views.send_mail_with_excel, name="send_mail_with_excel"),
    path('expensas/', views.expensas, name='expensas'),
    path('expensas/create/', views.create_expensa, name="crear_expensa"),
    path('expensas/<int:gasto_id>/', views.expensa_detail, name='expensa_detail'),
    path('expensas/<int:gasto_id>/delete/', views.delete_expensa, name='delete_expensa'),
    path('expensas/export_excel', views.expensas_export_excel, name="expensas_export_excel"),
    path('expensas/export_excel_gmail', views.expensas_send_mail_with_excel, name="expensas_send_mail_with_excel"),
    path('logout/', views.signout, name='logout'),
    path('search-expenses', csrf_exempt(views.search_expenses),
         name="search_expenses"),
    path('signin/', views.signin, name='signin')
]
