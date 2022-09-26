from django.contrib import admin

# Register your models here.
from measurement.models import Sensor, Measurement

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']

@admin.register(Measurement)
class MeasurmentAdmin(admin.ModelAdmin):
    list_display = ['temperature', 'created_at', 'image']
