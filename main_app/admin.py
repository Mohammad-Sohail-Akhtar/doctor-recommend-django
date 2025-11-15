from django.contrib import admin
from .models import Speciality, Doctor, Appointment

# Register your models here.
# class SpecialityAdmin(admin.ModelAdmin):
#     list_display = ('name', 'image_path')


admin.site.register(Speciality)
admin.site.register(Doctor)
admin.site.register(Appointment) 
