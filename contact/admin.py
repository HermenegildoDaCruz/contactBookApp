from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.contact)
class ContactAdmin(admin.ModelAdmin):
   list_display = 'id','first_name','description','email', # select em django
   ordering = '-id', #order by first_name em django
   search_fields = 'id','first_name'

   #list_filter = 'created_date',
   #list_per_page = 1
   #list_max_show_all = 100
   #list_editable = 'first_name',
   list_display_links = 'id','email',
