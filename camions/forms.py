from django import forms
from .models import Camion, Trajet, Entretien, Depense, Revenu

class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ['immatriculation', 'marque', 'modele', 'capacite', 'etat', 'assurance', 'controle_technique']

class TrajetForm(forms.ModelForm):
    class Meta:
        model = Trajet
        fields = ['date', 'heure', 'distance', 'destination', 'chauffeur', 'camion']

class EntretienForm(forms.ModelForm):
    class Meta:
        model = Entretien
        fields = ['camion', 'date', 'type', 'cout', 'pieces_remplacees']

class DepenseForm(forms.ModelForm):
    class Meta:
        model = Depense
        fields = ['type', 'montant', 'date', 'camion', 'chauffeur']

class RevenuForm(forms.ModelForm):
    class Meta:
        model = Revenu
        fields = ['camion', 'montant', 'type', 'date', 'distance', 'poids', 'tarif']
