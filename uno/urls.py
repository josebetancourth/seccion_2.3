"""uno URL Configuration

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

from uno.view import calculo, fecha, hola
from uno.view2 import fecha2, lista, saludar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/',hola),
    path('fecha/',fecha),
    path('calculo/<int:nacimiento>/<int:futuro>/',calculo),
    path('saludar/',saludar),
    path('fecha2/',fecha2),
    path('lista/',lista)
]
