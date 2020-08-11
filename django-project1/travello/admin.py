from django.contrib import admin
from travello.models import Destination
# Register your models here.
class DestinationAdmin(admin.ModelAdmin):
    list_display=['id','name','price','desc','img']

admin.site.register(Destination,DestinationAdmin)