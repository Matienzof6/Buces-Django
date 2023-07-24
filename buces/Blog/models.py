from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True) #Para agregar la fecha automaticamente auto_now_add
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'

    def __str__(self):
        
        return self.nombre



class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=250)
    imagen=models.ImageField(upload_to='Blog', null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now_add=True) #Para agregar la fecha automaticamente auto_now_add
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'

    def __str__(self):
        
        return self.titulo