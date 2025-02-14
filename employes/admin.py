from django.contrib import admin
from .models import Employe

@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'contact', 'role', 'salaire')
    search_fields = ('nom', 'prenom', 'contact', 'role')
    list_filter = ('role',)
