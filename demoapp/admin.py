from django.contrib import admin
from . models import Employee,Question,Choice

# Register your models here.
admin.site.register(Employee)
admin.site.register(Question)
admin.site.register(Choice)