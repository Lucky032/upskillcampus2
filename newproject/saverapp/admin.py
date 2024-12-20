from django.contrib import admin
from .models import Personalinfo,PasswordEntry

@admin.register(Personalinfo)
class PersonalinfoAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password']
    search_fields = ['username', 'email', 'password']
    add_form = Personalinfo
    add_fieldsets = (
        (None, {
            'fields': ('username','email', 'password')
        }))

@admin.register(PasswordEntry)
class PasswordEntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'website', 'username', 'password']
    search_fields = ['website', 'username', 'password']
    
    
