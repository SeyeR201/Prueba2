from django.shortcuts import render

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

