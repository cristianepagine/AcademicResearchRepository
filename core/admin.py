from django.contrib import admin
from core.models import Registers

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('title', 'category__name',)
    search_fields = ('title', 'category__name', 'autors')

    
admin.site.register(Registers, RegistrationAdmin)