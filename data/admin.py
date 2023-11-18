from django.contrib import admin
from data.models import user, homephoto,textile,jewellery,vegetable,other

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile','message')

admin.site.register(user, UserAdmin)

class PhotohomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'photos')

admin.site.register(homephoto, PhotohomeAdmin)

class TextileAdmin(admin.ModelAdmin):
    list_display = ('id', 'photos', 'name', 'message','size','size1','size2','size3','mainprice','discount','realprice')

admin.site.register(textile, TextileAdmin)

class JewelleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'photos', 'name', 'message','mainprice','discount','realprice')

admin.site.register(jewellery, JewelleryAdmin)

class VegetableAdmin(admin.ModelAdmin):
    list_display = ('id', 'photos', 'name', 'kg','mainprice','discount','realprice')

admin.site.register(vegetable, VegetableAdmin)

class OtherAdmin(admin.ModelAdmin):
    list_display = ('id', 'photos', 'name', 'message','size','size1','size2','size3','mainprice','discount','realprice')

admin.site.register(other, OtherAdmin)

