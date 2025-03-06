from django.contrib import admin
from .models import Record
# Register your models here.
class RecordAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone','address','city','zip_code','created_at']
    search_fields = ['first_name','last_name','email','phone','address','city','zip_code','created_at']
    list_filter = ['created_at']

admin.site.register(Record,RecordAdmin)