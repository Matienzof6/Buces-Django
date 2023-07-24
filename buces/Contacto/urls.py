from django.urls import path
from Contacto import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('', views.contact, name='Contact'),

]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)