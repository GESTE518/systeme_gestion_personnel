from django.contrib import admin
from .models import Camion, Trajet, Entretien, Depense, Revenu
from employes.models import Employe  # Pour affichage éventuel du chauffeur

@admin.register(Camion)
class CamionAdmin(admin.ModelAdmin):
    list_display = ('immatriculation', 'marque', 'modele', 'capacite', 'etat')
    inlines = []  # Aucun inline pour simplifier le formulaire d'ajout


@admin.register(Trajet)
class TrajetAdmin(admin.ModelAdmin):
    list_display = ('date', 'heure', 'distance', 'destination', 'chauffeur', 'camion')
    
    # Optionnel : méthode pour afficher le nom complet du chauffeur
    def chauffeur(self, obj):
        return f"{obj.chauffeur.nom} {obj.chauffeur.prenom}"
    chauffeur.short_description = "Chauffeur"


@admin.register(Entretien)
class EntretienAdmin(admin.ModelAdmin):
    list_display = ('date', 'type', 'cout', 'camion')


@admin.register(Depense)
class DepenseAdmin(admin.ModelAdmin):
    list_display = ('type', 'montant', 'date', 'chauffeur', 'camion')

    def chauffeur(self, obj):
        return f"{obj.chauffeur.nom} {obj.chauffeur.prenom}"
    chauffeur.short_description = "Chauffeur"


@admin.register(Revenu)
class RevenuAdmin(admin.ModelAdmin):
    # Affichage mis à jour pour refléter le rattachement au camion
    list_display = ('camion', 'montant', 'type', 'date', 'distance', 'poids', 'tarif')
