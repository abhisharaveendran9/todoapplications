from django.contrib import admin

# Register your models here.

from todoapp.models import Todos
admin.site.register(Todos)