from django.contrib import admin
from .models import Person
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display=('id','name','past_job')
admin.site.register(Person, PersonAdmin)