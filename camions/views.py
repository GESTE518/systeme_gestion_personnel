from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Camion, Trajet, Entretien, Depense, Revenu
from .forms import CamionForm, TrajetForm, EntretienForm, DepenseForm, RevenuForm
from .reports import generate_report  # Assurez-vous que vous avez une fonction de génération de rapports
from django.db.models import Sum

# Camion Views
def camion_list(request):
    camions = Camion.objects.all()
    return render(request, 'camions/camion_list.html', {'camions': camions})



def camion_detail(request, pk):
    camion = get_object_or_404(Camion, pk=pk)
    depenses = Depense.objects.filter(camion=camion)
    revenus = Revenu.objects.filter(camion=camion)
    entretiens = Entretien.objects.filter(camion=camion)

    total_depenses = depenses.aggregate(total=Sum('montant'))['total'] or 0
    total_revenus = revenus.aggregate(total=Sum('montant'))['total'] or 0
    solde = total_revenus - total_depenses  # Ou ajuster selon votre logique

    context = {
        'camion': camion,
        'trajets': Trajet.objects.filter(camion=camion),
        'depenses': depenses,
        'revenus': revenus,
        'entretiens': entretiens,
        'total_depenses': total_depenses,
        'total_revenus': total_revenus,
        'solde': solde,
    }
    return render(request, 'camions/camion_detail.html', context)


def camion_create(request):
    form = CamionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('camions:camion_list')
    return render(request, 'camions/camion_form.html', {'form': form})

def camion_edit(request, pk):
    camion = get_object_or_404(Camion, pk=pk)
    form = CamionForm(request.POST or None, instance=camion)
    if form.is_valid():
        form.save()
        return redirect('camions:camion_list')
    return render(request, 'camions/camion_form.html', {'form': form})

def camion_delete(request, pk):
    camion = get_object_or_404(Camion, pk=pk)
    if request.method == 'POST':
        camion.delete()
        return redirect('camions:camion_list')
    return render(request, 'camions/camion_confirm_delete.html', {'camion': camion})


# Trajet Views
def trajet_list(request):
    trajets = Trajet.objects.all()
    return render(request, 'camions/trajet_list.html', {'trajets': trajets})

def trajet_detail(request, pk):
    trajet = get_object_or_404(Trajet, pk=pk)
    return render(request, 'camions/trajet_detail.html', {'trajet': trajet})

def trajet_create(request):
    form = TrajetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('camions:trajet_list')
    return render(request, 'camions/trajet_form.html', {'form': form})

def trajet_edit(request, pk):
    trajet = get_object_or_404(Trajet, pk=pk)
    form = TrajetForm(request.POST or None, instance=trajet)
    if form.is_valid():
        form.save()
        return redirect('camions:trajet_list')
    return render(request, 'camions/trajet_form.html', {'form': form})

def trajet_delete(request, pk):
    trajet = get_object_or_404(Trajet, pk=pk)
    if request.method == 'POST':
        trajet.delete()
        return redirect('camions:trajet_list')
    return render(request, 'camions/trajet_confirm_delete.html', {'trajet': trajet})

# Entretien Views
def entretien_list(request):
    entretiens = Entretien.objects.all()
    return render(request, 'camions/entretien_list.html', {'entretiens': entretiens})

def entretien_create(request):
    form = EntretienForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('camions:entretien_list')
    return render(request, 'camions/entretien_form.html', {'form': form})

def entretien_delete(request, pk):
    entretien = get_object_or_404(Entretien, pk=pk)
    if request.method == 'POST':
        entretien.delete()
        return redirect('camions:entretien_list')
    return render(request, 'camions/entretien_confirm_delete.html', {'entretien': entretien})


# Liste des dépenses
def depense_list(request):
    depenses = Depense.objects.all()
    return render(request, 'camions/depense_list.html', {'depenses': depenses})

# Création d'une dépense
def depense_create(request):
    form = DepenseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('camions:depense_list')
    return render(request, 'camions/depense_form.html', {'form': form})

# Modification d'une dépense
def depense_update(request, pk):
    depense = get_object_or_404(Depense, pk=pk)
    form = DepenseForm(request.POST or None, instance=depense)
    if form.is_valid():
        form.save()
        return redirect('camions:depense_list')
    return render(request, 'camions/depense_form.html', {'form': form})

# Suppression d'une dépense
def depense_delete(request, pk):
    depense = get_object_or_404(Depense, pk=pk)
    if request.method == 'POST':
        depense.delete()
        return redirect('camions:depense_list')
    return render(request, 'camions/depense_confirm_delete.html', {'depense': depense})


# Revenu Views
def revenu_list(request):
    revenus = Revenu.objects.all()
    return render(request, 'camions/revenu_list.html', {'revenus': revenus})

def revenu_create(request):
    form = RevenuForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('camions:revenu_list')
    return render(request, 'camions/revenu_form.html', {'form': form})

def revenu_delete(request, pk):
    revenu = get_object_or_404(Revenu, pk=pk)
    if request.method == 'POST':
        revenu.delete()
        return redirect('camions:revenu_list')
    return render(request, 'camions/revenu_confirm_delete.html', {'revenu': revenu})

from django.shortcuts import render
from django.http import HttpResponse
from .models import Camion, Trajet, Entretien, Depense, Revenu
import logging

logger = logging.getLogger(__name__)

def generate_camion_report(start_date, end_date):
    """Génère le rapport des camions sur une période donnée."""
    try:
        # Récupération de tous les camions et filtrage des autres modèles par période
        camions = Camion.objects.all()
        trajets = Trajet.objects.filter(date__range=[start_date, end_date])
        entretiens = Entretien.objects.filter(date__range=[start_date, end_date])
        depenses = Depense.objects.filter(date__range=[start_date, end_date])
        revenus = Revenu.objects.filter(date__range=[start_date, end_date])

        # Calcul des statistiques globales
        total_revenus = sum(revenu.montant for revenu in revenus)
        total_depenses = sum(depense.montant for depense in depenses)
        global_benefit = total_revenus - total_depenses

        # Calcul des statistiques par camion
        camion_stats = []
        for camion in camions:
            revenus_camion = sum(revenu.montant for revenu in revenus.filter(camion=camion))
            depenses_camion = sum(depense.montant for depense in depenses.filter(camion=camion))
            performance = revenus_camion - depenses_camion
            camion_stats.append({
                'camion': camion.immatriculation,
                'revenues': revenus_camion,
                'expenses': depenses_camion,
                'performance': performance
            })

        return {
            'total_revenues': total_revenus,
            'total_expenses': total_depenses,
            'global_benefit': global_benefit,
            'camion_stats': camion_stats
        }
    except Exception as e:
        logger.error(f"Erreur lors de la génération du rapport camion: {e}")
        return None

def rapport_dashboard(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    try:
        report_data = generate_camion_report(start_date, end_date)
        if report_data is None:
            return HttpResponse("Erreur dans la génération des données", status=500)
    except Exception as e:
        logger.error(f"Erreur lors de la génération du rapport global: {e}")
        return HttpResponse(f"Erreur : {str(e)}", status=500)

    return render(request, 'rapports/dashboard.html', {
        'report_data': report_data,
        'request': request  # Pour accéder à request.GET dans le template
    })

def rapport_camion(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    try:
        report_data = generate_camion_report(start_date, end_date)
        if report_data is None:
            return HttpResponse("Erreur dans la génération des données", status=500)
    except Exception as e:
        logger.error(f"Erreur lors de la génération du rapport camion: {e}")
        return HttpResponse(f"Erreur : {str(e)}", status=500)

    return render(request, 'rapports/rapport_camion.html', {
        'report_data': report_data,
        'request': request
    })

# Les autres vues (camion_list, camion_create, etc.) doivent être définies ici.


        