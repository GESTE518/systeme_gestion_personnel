from django.db import models
from django.db.models import Sum
from employes.models import Employe  # Assurez-vous que le modèle Employe est bien défini dans l'application employes

class Cahier(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, verbose_name="Employé")

    def __str__(self):
        return f"Cahier de {self.employe}"

    @property
    def total_biens(self):
        """Somme totale des prix des biens apportés."""
        total = self.echangebiens_set.aggregate(total=Sum('prix'))['total']
        return total or 0

    @property
    def total_avances(self):
        """Somme totale des montants des avances."""
        total = self.avanceargent_set.aggregate(total=Sum('montant'))['total']
        return total or 0

    @property
    def solde(self):
        """
        Calcule le solde :
         - Solde positif : l'employé vous doit de l'argent (crédit)
         - Solde négatif : vous devez de l'argent à l'employé (dette)
        """
        return self.total_avances - self.total_biens

    @property
    def statut_solde(self):
        """Renvoie un libellé indiquant si le solde est en crédit, en dette ou équilibré."""
        if self.solde < 0:
            return "Dette"
        elif self.solde > 0:
            return "Crédit"
        else:
            return "Équilibré"


class AvanceArgent(models.Model):
    cahier = models.ForeignKey(Cahier, on_delete=models.CASCADE)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    statut = models.CharField(max_length=50)
    pdf = models.FileField(upload_to='pdfs/avances/', blank=True, null=True)

    def __str__(self):
        return f"Avance de {self.montant}€ le {self.date}"


class EchangeBiens(models.Model):
    cahier = models.ForeignKey(Cahier, on_delete=models.CASCADE)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    nom_bien = models.CharField(max_length=200)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    statut = models.CharField(max_length=50)
    pdf = models.FileField(upload_to='pdfs/echanges/', blank=True, null=True)

    def __str__(self):
        return f"{self.nom_bien} ({self.prix}€) le {self.date}"
