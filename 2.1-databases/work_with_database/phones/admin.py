from django.contrib import admin

# Register your models here.
from .models import Phone

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
