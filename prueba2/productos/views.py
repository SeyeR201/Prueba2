from django.shortcuts import render
from .models import Producto

# Create your views here.

def index(request):
    print("vista: index.")
    context={}
    return render(request, 'productos/index.html', context)

def products(request):
    print("vista: products")
    context={}
    return render(request, 'productos/products.html', context)

def beyond(request):
    print("vista: beyond")
    context={}
    return render(request, 'productos/beyond.html', context)

def conservas(request):
    print("vista: conservas")
    context={}
    return render(request, 'productos/conservas.html', context)

def quesos(request):
    print("vista: quesos")
    context={}
    return render(request, 'productos/quesos.html', context)

def agregar(request):
    print("vista: agregar")
    context={}
    return render(request, 'productos/agregar_producto.html', context)

def agregar_productos(request):
    print("vista: agregar productos")
    if request.method == 'POST':
       mi_codigo = request.POST['codigo']
       mi_nombre= request.POST['nombre']
       mi_descripcion =request.POST['descripcion']
       mi_precio =request.POST['precio']
       mi_stock =request.POST['stock']
       mi_foto = request.FILES['foto']

       if mi_codigo != "":
           try:
               producto = Producto()

               producto.codigo = mi_codigo
               producto.nombre_producto = mi_nombre
               producto.descripcion_producto = mi_descripcion
               producto.precio = mi_precio
               producto.stock = mi_stock
               producto.foto_producto = mi_foto

               producto.save()

               return render(request, 'productos/producto_agregado.html',{})

           except producto.DoesNotExist:
               return render(request, 'productos/error.html', {})
       else:
           return render(request, 'productos/error.html', {})
    else:
        return render(request, 'productos/error.html', {})

def eliminar(request):
    print("ok, vista: eliminar")
    context={}
    return render(request,'productos/eliminar_producto.html',context)

def eliminar_producto(request):
    print("vista: eliminar producto")
    if request.method == 'POST':
       mi_codigo = request.POST['codigo']

       if mi_codigo != "":
           try:
               producto = Producto()
               producto= Producto.objects.get(codigo=mi_codigo)
               if producto is not None:
                   print("Producto=", producto)
                   producto.delete()

                   return render(request, 'productos/producto_eliminado.html',{})
               else:
                   return render(request, 'productos/error.html',{})
           except producto.DoesNotExist:
               return render(request, 'productos/error.html', {})
       else:
           return render(request, 'productos/error.html', {})
    else:
        return render(request, 'productos/error.html', {})

def editar(request):
    print("ok, vista: editar")
    context={}
    return render(request,'productos/editar_producto.html',context)

def editar_producto(request):
    print("vista: editar producto")
    if request.method == 'POST':
       mi_codigo = request.POST['codigo']

       if mi_codigo != "":
           try:
               producto = Producto()
               producto= Producto.objects.get(codigo=mi_codigo)
               if producto is not None:
                   print("Producto=", producto)
                   context={'producto':producto}
                   return render(request, 'productos/formulario_editar.html', context)
               else:
                   return render(request, 'productos/error.html',{})
           except producto.DoesNotExist:
               return render(request, 'productos/error.html', {})
       else:
           return render(request, 'productos/error.html', {})
    else:
        return render(request, 'productos/error.html', {})

def editar_productos(request):
    print("vista: editar productos")
    if request.method == 'POST':
        mi_codigo = request.POST['codigo']
        mi_nombre = request.POST['nombre']
        mi_descripcion = request.POST['descripcion']
        mi_precio = request.POST['precio']
        mi_stock = request.POST['stock']
        mi_foto = request.FILES['foto']

        if mi_codigo != "":
            try:
                producto = Producto()

                producto.codigo = mi_codigo
                producto.nombre_producto = mi_nombre
                producto.descripcion_producto = mi_descripcion
                producto.precio = mi_precio
                producto.stock = mi_stock
                producto.foto_producto = mi_foto

                producto.save()#actualiza al comprobar que codigo ya existe

                return render(request, 'productos/producto_editado.html', {})

            except producto.DoesNotExist:
                return render(request, 'productos/error.html', {})
        else:
            return render(request, 'productos/error.html', {})

    else:
        return render(request, 'productos/error.html', {})


def mostrar_productos(request):
    print("vista: mostrar_productos")
    lista = Producto.objects.all()
    context={'listado': lista}
    return render(request, 'productos/listar_productos.html', context)