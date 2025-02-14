from django import forms
from .models import AvanceArgent, EchangeBiens, Cahier  # Vérifie que le modèle Cahier existe

class AvanceArgentForm(forms.ModelForm):
    class Meta:
        model = AvanceArgent
        fields = ['montant', 'date', 'statut', 'pdf']

class EchangeBiensForm(forms.ModelForm):
    class Meta:
        model = EchangeBiens
        fields = ['nom_bien', 'prix', 'date', 'statut', 'pdf']

# Ajout de CahierForm si nécessaire
class CahierForm(forms.ModelForm):
    class Meta:
        model = Cahier
        fields = '__all__'  # Ou spécifie les champs nécessaires
