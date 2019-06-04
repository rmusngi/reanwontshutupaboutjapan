from django.contrib import admin
from .models import destination

class DestinationAdmin(admin.ModelAdmin):
    list_display=('id')
    
admin.site.register(destination)