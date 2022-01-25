from django.contrib import admin
from . import models

admin.site.register(models.Contact)
#@admin.register(models.Model)
#class ContactAdmin(admin.ModelAdmin):
#    list_display = ('first_name', 'last_name', 'phone', 'email')
