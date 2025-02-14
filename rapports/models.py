from django.db.models import Sum
from camions.models import Revenu, Depense, Camion

def global_report():
    """
    Retourne le rapport global de l'entreprise basé sur les données des revenus et dépenses des camions :
    - Total des revenus
    - Total des dépenses
    - Bénéfice global (revenus - dépenses)
    """
    total_revenues = Revenu.objects.aggregate(total=Sum('montant'))['total'] or 0
    total_expenses = Depense.objects.aggregate(total=Sum('montant'))['total'] or 0
    global_benefit = total_revenues - total_expenses

    return {
        'total_revenues': total_revenues,
        'total_expenses': total_expenses,
        'global_benefit': global_benefit,
    }

def camion_performance():
    """
    Retourne la performance de chaque camion sous forme d'une liste de dictionnaires.
    Pour chaque camion, on calcule :
      - Le total des revenus associés
      - Le total des dépenses associées
      - La performance = revenus - dépenses
    """
    performance_list = []
    for camion in Camion.objects.all():
        revenues = Revenu.objects.filter(camion=camion).aggregate(total=Sum('montant'))['total'] or 0
        expenses = Depense.objects.filter(camion=camion).aggregate(total=Sum('montant'))['total'] or 0
        performance = revenues - expenses
        performance_list.append({
            'camion': camion,
            'revenues': revenues,
            'expenses': expenses,
            'performance': performance,
        })
    return performance_list

# Vous pouvez ajouter d'autres fonctions de rapports ici si nécessaire.
