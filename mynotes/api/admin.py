from django.contrib import admin
from .models import Note

# Register your models here.

# To show the Note  table in admin panel of Django we do this 
admin.site.register(Note)
