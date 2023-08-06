from django.contrib import admin

# Register your models here.
from .models import Make, Auto

admin.site.register(Auto)
admin.site.register(Make)