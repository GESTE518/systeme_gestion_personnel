from django.db import models
from employes.models import Employe  # Pour le champ chauffeur
# La ligne suivante n'est plus nécessaire si on ne lie plus Revenu à Client
# from clients.models import Client  

class Camion(models.Model):
    immatriculation = models.CharField(max_length=15, unique=True)
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    capacite = models.DecimalField(max_digits=10, decimal_places=2)
    etat = models.CharField(max_length=50)
    assurance = models.DateField()
    controle_technique = models.DateField()

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.immatriculation})"


class Trajet(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    destination = models.CharField(max_length=200)
    chauffeur = models.ForeignKey(Employe, on_delete=models.CASCADE)  # Référence directe à Employe
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Trajet {self.date} à {self.heure} vers {self.destination}"


class Entretien(models.Model):
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
    date = models.DateField()
    type = models.CharField(max_length=100)
    cout = models.DecimalField(max_digits=10, decimal_places=2)
    pieces_remplacees = models.TextField()

    def __str__(self):
        return f"Entretien {self.date} sur {self.camion}"


class Depense(models.Model):
    TYPE_CHOICES = [
        ('Carburant', 'Carburant'),
        ('Peages', 'Peages'),
        ('Reparations', 'Reparations'),
        ('Salaires', 'Salaires'),
    ]
    
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
    chauffeur = models.ForeignKey(Employe, on_delete=models.CASCADE)  # Référence directe à Employe

    def __str__(self):
        return f"{self.type} le {self.date} pour {self.camion}"


class Revenu(models.Model):
    # Changement : le revenu est rattaché à un Camion et non à un Client
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=100)
    date = models.DateField()
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    poids = models.DecimalField(max_digits=10, decimal_places=2)
    tarif = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Revenu de {self.montant}€ le {self.date} pour {self.camion}"
