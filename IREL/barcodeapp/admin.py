from django.contrib import admin
from .models import *

admin.site.register(Department)
admin.site.register(Product)
admin.site.register(Exit)
# admin.site.register(Purchaserequisition)
admin.site.register(Rack)
admin.site.register(Shelf)
admin.site.register(Stock)
admin.site.register(Godown)
admin.site.register(ShelfSticker)
admin.site.register(ProductSticker)
admin.site.register(Inspection)