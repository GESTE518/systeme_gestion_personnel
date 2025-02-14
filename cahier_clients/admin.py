from django.contrib import admin
from .models import Cahier, AvanceArgent, EchangeBiens

class AvanceArgentInline(admin.TabularInline):
    model = AvanceArgent
    extra = 1


class EchangeBiensInline(admin.TabularInline):
    model = EchangeBiens
    extra = 1


@admin.register(Cahier)
class CahierAdmin(admin.ModelAdmin):
    list_display = ('employe', 'total_biens', 'total_avances', 'solde', 'statut_solde')
    inlines = []
    search_fields = ('employe__nom', 'employe__prenom')  # ajustez selon les champs du modèle Employe


@admin.register(AvanceArgent)
class AvanceArgentAdmin(admin.ModelAdmin):
    list_display = ('cahier', 'employe', 'montant', 'date', 'statut')
    list_filter = ('date', 'statut')
    search_fields = ('cahier__employe__nom', 'cahier__employe__prenom')


@admin.register(EchangeBiens)
class EchangeBiensAdmin(admin.ModelAdmin):
    list_display = ('cahier', 'employe', 'nom_bien', 'prix', 'date', 'statut')
    list_filter = ('date', 'statut')
    search_fields = ('cahier__employe__nom', 'cahier__employe__prenom', 'nom_bien')
