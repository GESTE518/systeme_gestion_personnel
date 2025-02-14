# camions/reports.py

from .models import Camion, Trajet, Entretien, Depense, Revenu

def generate_report(start_date=None, end_date=None):
    revenus = Revenu.objects.all()
    depenses = Depense.objects.all()

    # Filtrer les données selon les dates fournies
    if start_date:
        revenus = revenus.filter(date__gte=start_date)
        depenses = depenses.filter(date__gte=start_date)
    if end_date:
        revenus = revenus.filter(date__lte=end_date)
        depenses = depenses.filter(date__lte=end_date)

    report_data = {
        'revenus': revenus,
        'depenses': depenses,
        'total_revenus': sum(r.montant for r in revenus),
        'total_depenses': sum(d.montant for d in depenses),
    }

    return report_data
