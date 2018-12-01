from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from .models import *
from .filters import ProductFilter
import barcode
from barcode.writer import ImageWriter
import csv
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
    return render(request,'barcodeapp/index.html')


def postproduct(request):
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            stock_item=form.save(commit=False)
            stock_item.save()
    else:
        form=ProductForm()
        return render(request,'barcodeapp/productentry.html',{'form':form})

def poststock(request):
    if request.method=="POST":
        form=StockForm(request.POST)
        if form.is_valid():
            stock_item=form.save(commit=False)
            stock_item.save()
    else:
        form=StockForm()
        form1=ProductForm()
        return render(request,'barcodeapp/stockform.html',{'form':form,'form1':form1})

def shelfstiker(request):
    if request.method=='POST':
        form=ShelfstickerForm(request.POST)
        if form.is_valid():
            product_item=form.save(commit=False)
            product_item.save()
    else:
        form=ShelfstickerForm()
        return render(request,'barcodeapp/shelfsticker.html',{'form':form})

def shelfbarcodecreate(request):
    barcode=Shelfsticker.objects.all()
    context={'barcode':barcode}
    return render(request,'barcodeapp/shelfbarcodeshower.html',context)


def productsticker(request):
    if request.method=='POST':
        form=ProductstickerForm(request.POST)
        if form.is_valid():
            product_item=form.save(commit=False)
            product_item.save()
    else:
        form=ProductstickerForm()
        return render(request, 'barcodeapp/productsticker.html', {'form': form})

def productbarcodecreate(request):
    barcode1=Product.objects.all()
    context={'barcode':barcode1,'module':barcode}
    # from . import mybarcode
    # for i in barcode:
    #     d = mybarcode.MyBarcodeDrawing(i.barcode)
    #     binaryStuff = d.asString('gif')
    #     return HttpResponse(filename 'image/gif')
    return render(request,'barcodeapp/productbarcodeshower.html',context)

# def barcode(request):
#     #instantiate a drawing object
#     import mybarcode
#     d = mybarcode.MyBarcodeDrawing("HELLO WORLD")
#     binaryStuff = d.asString('gif')
#     return HttpResponse(binaryStuff, 'image/gif')


# def productdetails(request):
#     # item=Product.objects.filter(id=id)
#     return render(request,'barcodeapp/productdetails.html')

def search(request):
    product_list = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=product_list)
    return render(request, 'barcodeapp/productdetails.html', {'filter': product_filter})

def exit(request):
    exit=Exit.objects.all()
    return render(request,'barcodeapp/exit.html',{'exit':exit})

def inspection(request):
    inspection=Inspection.objects.all()
    return render(request,'barcodeapp/inspection.html',{'inspection':inspection})

def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'First name', 'Last name', 'Email address'])

    users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for user in users:
        writer.writerow(user)

    return response