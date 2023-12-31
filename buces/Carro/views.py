from django.shortcuts import render
from .carro import Carro
from Tienda.models import Producto
from django.shortcuts import redirect
# Create your views here.


def agregar_producto(request, producto_id):
    
    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.agregar(producto=producto)
    

    if request.user.is_authenticated:
        return redirect("Shop")
    else:
        return redirect("carrito")

def aumentar_producto(request, producto_id):
    
    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.agregar(producto=producto)

    return redirect("carrito")




def eliminar_producto(request, producto_id):
    
    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.eliminar(producto=producto)

    return redirect("carrito")




def restar_producto(request, producto_id):
    
    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)

    return redirect("carrito")




def limpiar_carro(request):
    
    carro=Carro(request)

    carro.limpiar_carro()

    return redirect("carrito")
