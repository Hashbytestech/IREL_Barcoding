from django.shortcuts import render


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


import traceback



def index(request):
    return render(request,'barcodeapp/index.html')



def productsticker(request,id):	
    x, y = 0, 0

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="barcode.pdf"'

    c = canvas.Canvas(response)
    width, height = 60*mm, 25*mm
    c = canvas.Canvas(response, pagesize = (width, height))

    barcode = code128.Code128(id,barHeight=10*mm,barWidth = 1.0)
    barcode.drawOn(c, (x-1)*mm, (y+10)*mm)


    wd = c.stringWidth('aa', "Helvetica", 8)
    w = 18 - (wd*0.264583333)/2

    c.setFont("Helvetica-Bold",8)
    c.drawString((x+6)*mm, (y+5)*mm, "PRODUCT NO: "+id)

    c.showPage()
    c.save()

    return HttpResponse(response, content_type='application/pdf')


def product_barcode(request,id):
	return render(request,'asset/index.html',{'bid':id})





def selfsticker(request,id): 
    x, y = 0, 0

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="barcode.pdf"'

    c = canvas.Canvas(response)
    width, height = 60*mm, 25*mm
    c = canvas.Canvas(response, pagesize = (width, height))

    barcode = code128.Code128(id,barHeight=10*mm,barWidth = 1.0)
    barcode.drawOn(c, (x-1)*mm, (y+10)*mm)


    wd = c.stringWidth('aa', "Helvetica", 8)
    w = 18 - (wd*0.264583333)/2

    c.setFont("Helvetica-Bold",8)
    c.drawString((x+6)*mm, (y+5)*mm, "SELF NO: "+id)

    c.showPage()
    c.save()

    return HttpResponse(response, content_type='application/pdf')


def self_barcode(request,id):

    if request.is_secure():
        scheme = 'https://'
    else:
        scheme = 'http://'
        
    url =scheme + request.get_host()
    return render(request,'asset/self_barcode.html',{'bid':id})
