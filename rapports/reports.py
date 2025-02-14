# reports.py
from django.db.models import Sum
from camions.models import Revenu, Depense, Camion
from employes.models import Employe
from cahier_clients.models import Cahier  # Application de gestion des cahiers clients

def global_report():
    """
    Retourne le rapport global de l'entreprise :
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
    Retourne la performance de chaque camion sous forme d'une liste de dictionnaires,
    avec pour chacun :
    - Le camion
    - Le total des revenus qui lui sont rattachés
    - Le total des dépenses qui lui sont rattachés
    - La performance = revenus - dépenses
    """
    performance_list = []
    for camion in Camion.objects.all():
        revenues = Revenu.objects.filter(camion=camion).aggregate(total=Sum('montant'))['total'] or 0
        expenses = Depense.objects.filter(camion=camion).aggregate(total=Sum('montant'))['total'] or 0
        perf = revenues - expenses
        performance_list.append({
            'camion': camion,
            'revenues': revenues,
            'expenses': expenses,
            'performance': perf,
        })
    return performance_list

def employee_report():
    """
    Retourne le rapport pour chaque employé (basé sur l'application Cahier_clients) :
    - L'employé
    - Le total des avances d'argent et des biens via son cahier (calculé dans Cahier.solde)
      Le solde (total_avances - total_biens) indique :
         * Un solde positif : l'employé vous doit (crédit)
         * Un solde négatif : vous devez à l'employé (dette)
    """
    reports = []
    for emp in Employe.objects.all():
        try:
            # On part du principe qu'il existe un Cahier par employé.
            cahier = Cahier.objects.get(employe=emp)
            solde = cahier.solde  # Propriété calculée dans le modèle Cahier
        except Cahier.DoesNotExist:
            solde = 0  # Pas de données de cahier, on considère 0

        reports.append({
            'employee': emp,
            'solde': solde,
            'statut': 'Crédit' if solde > 0 else 'Dette' if solde < 0 else 'Équilibré'
        })
    return reports

# Exemple d'utilisation (par exemple, dans une vue Django ou une commande personnalisée)
if __name__ == '__main__':
    # Affichage du rapport global
    global_stats = global_report()
    print("Rapport global de l'entreprise:")
    print(f"  Revenus totaux : {global_stats['total_revenues']} €")
    print(f"  Dépenses totales : {global_stats['total_expenses']} €")
    print(f"  Bénéfice global : {global_stats['global_benefit']} €")
    print("\nPerformance par camion:")
    for perf in camion_performance():
        print(f"  Camion {perf['camion']}: Revenus = {perf['revenues']} €, Dépenses = {perf['expenses']} €, Performance = {perf['performance']} €")
    print("\nRapport par employé (via Cahier_clients):")
    for rep in employee_report():
        print(f"  Employé {rep['employee']}: Solde = {rep['solde']} € ({rep['statut']})")
