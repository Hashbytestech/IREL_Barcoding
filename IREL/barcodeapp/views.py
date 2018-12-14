from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from .models import *
from .filters import ProductFilter
import barcode
from barcode.writer import ImageWriter
import csv
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect





from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import mm, inch
from reportlab.graphics.barcode import code128

# from easy_pdf.views import PDFTemplateView
from xhtml2pdf import pisa


# import cStringIO as StringIO
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import HttpResponse

from django.http import HttpResponse
# Create your views here.

import sys ,traceback
# Create your views here.

import traceback




def index(request):
    return render(request,'barcodeapp/index.html')


# def postproduct(request):
#     if request.method=="POST":
#         form=ProductForm(request.POST)
#         if form.is_valid():
#             stock_item=form.save(commit=False)
#             stock_item.save()
#     else:
#         form=ProductForm()
#         return render(request,'barcodeapp/productentry.html',{'form':form})

def productlist(request):
    products=Product.objects.all()
    context={'product':products}
    return render(request,'barcodeapp/productlist.html',context)

def postproduct(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProductForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            product_item=form.save(commit=True)
            product_item.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/productlist/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProductForm()

    return render(request, 'barcodeapp/productentry.html', {'form': form})

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

        godown = request.POST.get('godown')
        rack = request.POST.get('rack')
        shelf = request.POST.get('shelf')
        return redirect('/rbarcode/self_barcode/'+godown+rack+shelf)

        # form=ShelfstickerForm(request.POST)
        # if form.is_valid():
        #     product_item=form.save(commit=False)
        #     product_item.save()
    else:
        form=ShelfstickerForm()
        return render(request,'barcodeapp/shelfsticker.html',{'form':form})

def shelfbarcodecreate(request):
        if request.method=="POST":
            form=ShelfstickerForm(request.POST)
            if form.is_valid():
                self_item_sticker = form.save(commit=False)
                self_item_sticker.save()
        else:
            form=ShelfstickerForm()
            barcode=ShelfSticker.objects.all()
        #     context={'barcode':barcode}
        # return render(request,'barcodeapp/shelfbarcodeshower.html',context)

            print (barcode)


            x, y = 0, 0
            id = 'qweqwe123123'

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="shelfbarcode.pdf"'
            c = canvas.Canvas(response)
            width, height = 35*mm, 25*mm
            c = canvas.Canvas(response, pagesize = (width, height))

            for val in barcode.iterator():


                barcode = code128.Code128(str(val),barHeight=10*mm,barWidth = 1.0)
                barcode.drawOn(c, (x-1)*mm, (y+10)*mm)


                wd = c.stringWidth('aa', "Helvetica", 8)
                w = 18 - (wd*0.264583333)/2

                c.setFont("Helvetica-Bold",8)
                c.drawString((x+6)*mm, (y+5)*mm, "SELF NO: "+str(val))

                c.showPage()
            c.save()

            return HttpResponse(response, content_type='application/pdf')


def productsticker(request):

    if request.method=='POST':
        # print (request.POST.get('product_code'))
        pid = request.POST.get('product_code')
        try:
            pObj = Product.objects.filter(pk= pid)
            return redirect('/rbarcode/product_barcode/'+pObj[0].product_code)
        except: 
            return HttpResponse('None')
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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ExitForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            exit_item = form.save(commit=True)
            exit_item.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/exit/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ExitForm()

    return render(request, 'barcodeapp/exit.html', {'form': form})

def inspection(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InspectionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # form.save()
            inspection_item = form.save(commit=True)
            inspection_item.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/inspection/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InspectionForm()

    return render(request, 'barcodeapp/inspection.html', {'form': form})

def productstickerbarcode(request):

    barcode=ProductSticker.objects.all()
    x, y = 0, 0

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="shelfbarcode.pdf"'
    c = canvas.Canvas(response)
    width, height = 70*mm, 25*mm
    c = canvas.Canvas(response, pagesize = (width, height))

    for val in barcode.iterator():

        # print(val.product_code)
        sb=PurchaseOrder.objects.filter(productId = val.product_code)
        pbc = str(val.product_code) + str(sb[0].purchase_order_no)

        barcode = code128.Code128(str(pbc),barHeight=10*mm,barWidth = 1.0)
        barcode.drawOn(c, (x-2)*mm, (y+10)*mm)


        wd = c.stringWidth('aa', "Helvetica", 8)
        w = 18 - (wd*0.264583333)/2

        c.setFont("Helvetica-Bold",8)
        c.drawString((x+6)*mm, (y+5)*mm, "PRODUCT : "+str(pbc))

        c.showPage()
    c.save()

    return HttpResponse(response, content_type='application/pdf')

