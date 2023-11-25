"""
URL configuration for ProyectoMaraujo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from ProyectoMaraujo.views import saludo, saludo_html, saludo_nombre, saludo_plantilla


urlpatterns = [
    path('plantilla1/', saludo_plantilla),
    path('saludo/', saludo),
    path('saludoh/', saludo_html),
    path('saludo/<nombre>', saludo_nombre),
    path('admin/', admin.site.urls),
]
