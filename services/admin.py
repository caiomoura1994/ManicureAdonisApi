from django.contrib import admin
from .models import Category, Service, SubCategory, ServiceRegister

admin.site.register(Category)
admin.site.register(Service)
admin.site.register(SubCategory)
admin.site.register(ServiceRegister)
