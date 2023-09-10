from django.contrib import admin
from  . import models
# Register your models here.

admin.site.register(models.Clinic)
admin.site.register(models.Doctor)
admin.site.register(models.OpeningTime)
admin.site.register(models.Service)
admin.site.register(models.About)
admin.site.register(models.Testimonial)