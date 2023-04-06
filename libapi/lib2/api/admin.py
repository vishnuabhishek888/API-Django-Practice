from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
   list_display = ['id','name','roll','city']

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
   list_display = ['name','writer','quantity']

@admin.register(IssuedBook)
class IssuedBookAdmin(admin.ModelAdmin):
   list_display = ['student','book','quantity']