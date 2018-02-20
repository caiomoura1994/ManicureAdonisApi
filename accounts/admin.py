from django.contrib import admin

from .models import ServiceProviderProfile,ClientProfileProfile

admin.site.register(ServiceProviderProfile)
admin.site.register(ClientProfileProfile)