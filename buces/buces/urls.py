"""
URL configuration for buces project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ProyectoWebApp.views import home
from Servicios.views import services
from django.urls import include, re_path
from django.conf import settings
from django.views.static import serve

from Tienda.views import carroVista
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ProyectoWebApp.urls')),
    path('services/', include('Servicios.urls')),
    path('blog/', include('Blog.urls')),
    path('contact/', include('Contacto.urls')),
    path('shop/', include('Tienda.urls')),
    path('carro/', include('Carro.urls')),
    path('autenticacion/', include('Autenticacion.urls')),
    path('pedidos/', include('Pedidos.urls')),
    path('carrito/',carroVista, name='carrito'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)