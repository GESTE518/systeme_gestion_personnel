from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Cahier, AvanceArgent, EchangeBiens
from .forms import CahierForm, AvanceArgentForm, EchangeBiensForm
from employes.models import Employe  # Import du modèle Employe

# Liste des cahiers
def cahier_list(request):
    cahiers = Cahier.objects.all()
    return render(request, 'cahier_clients/cahier_list.html', {'cahiers': cahiers})

# Détails d'un cahier spécifique
def cahier_detail(request, pk):
    cahier = get_object_or_404(Cahier, pk=pk)
    avances = AvanceArgent.objects.filter(cahier=cahier)
    echanges = EchangeBiens.objects.filter(cahier=cahier)
    return render(request, 'cahier_clients/cahier_detail.html', {
        'cahier': cahier,
        'avances': avances,
        'echanges': echanges
    })

# Création d'un cahier
def cahier_create(request):
    employees = Employe.objects.all()  # Récupérer tous les employés
    if request.method == "POST":
        form = CahierForm(request.POST)
        if form.is_valid():
            cahier = form.save()
            return redirect('cahier_clients:cahier_detail', pk=cahier.pk)
    else:
        form = CahierForm()
    return render(request, 'cahier_clients/cahier_create.html', {'form': form, 'employees': employees})


# Modification d'un cahier
def cahier_edit(request, pk):
    cahier = get_object_or_404(Cahier, pk=pk)
    if request.method == "POST":
        form = CahierForm(request.POST, instance=cahier)
        if form.is_valid():
            form.save()
            return redirect('cahier_clients:cahier_detail', pk=cahier.pk)
    else:
        form = CahierForm(instance=cahier)
    return render(request, 'cahier_clients/cahier_edit.html', {'form': form, 'cahier': cahier})

# Suppression d'un cahier
def cahier_delete(request, pk):
    cahier = get_object_or_404(Cahier, pk=pk)
    cahier.delete()
    return redirect('cahier_clients:index')

# Ajouter une avance d'argent
def avance_argent_create(request, cahier_pk):
    cahier = get_object_or_404(Cahier, pk=cahier_pk)
    if request.method == 'POST':
        form = AvanceArgentForm(request.POST, request.FILES)
        if form.is_valid():
            avance = form.save(commit=False)
            avance.cahier = cahier
            avance.employe = cahier.employe  # Lier l'employé
            avance.save()
            return redirect('cahier_clients:cahier_detail', pk=cahier.pk)
    else:
        form = AvanceArgentForm()
    return render(request, 'cahier_clients/avance_argent_form.html', {'form': form, 'cahier': cahier})

# Modifier une avance d'argent
def avance_argent_edit(request, pk):
    avance = get_object_or_404(AvanceArgent, pk=pk)
    if request.method == 'POST':
        form = AvanceArgentForm(request.POST, request.FILES, instance=avance)
        if form.is_valid():
            form.save()
            return redirect('cahier_clients:cahier_detail', pk=avance.cahier.pk)
    else:
        form = AvanceArgentForm(instance=avance)
    return render(request, 'cahier_clients/avance_argent_form.html', {'form': form, 'avance': avance})

# Supprimer une avance d'argent
def avance_argent_delete(request, pk):
    avance = get_object_or_404(AvanceArgent, pk=pk)
    cahier = avance.cahier
    avance.delete()
    return redirect('cahier_clients:cahier_detail', pk=cahier.pk)

# Ajouter un échange de bien
def echange_biens_create(request, cahier_pk):
    cahier = get_object_or_404(Cahier, pk=cahier_pk)
    if request.method == 'POST':
        form = EchangeBiensForm(request.POST, request.FILES)
        if form.is_valid():
            echange = form.save(commit=False)
            echange.cahier = cahier
            echange.employe = cahier.employe  # Lier l'employé
            echange.save()
            return redirect('cahier_clients:cahier_detail', pk=cahier.pk)
    else:
        form = EchangeBiensForm()
    return render(request, 'cahier_clients/echange_biens_form.html', {'form': form, 'cahier': cahier})

# Modifier un échange de bien
def echange_biens_edit(request, pk):
    echange = get_object_or_404(EchangeBiens, pk=pk)
    if request.method == 'POST':
        form = EchangeBiensForm(request.POST, request.FILES, instance=echange)
        if form.is_valid():
            form.save()
            return redirect('cahier_clients:cahier_detail', pk=echange.cahier.pk)
    else:
        form = EchangeBiensForm(instance=echange)
    return render(request, 'cahier_clients/echange_biens_form.html', {'form': form, 'echange': echange})

# Supprimer un échange de bien
def echange_biens_delete(request, pk):
    echange = get_object_or_404(EchangeBiens, pk=pk)
    cahier = echange.cahier
    echange.delete()
    return redirect('cahier_clients:cahier_detail', pk=cahier.pk)



def rapport_global(request):
    cahiers = Cahier.objects.all()
    
    total_avances = sum(cahier.total_avances for cahier in cahiers)
    total_biens = sum(cahier.total_biens for cahier in cahiers)
    solde_global = total_avances - total_biens

    context = {
        "cahiers": cahiers,
        "total_avances": total_avances,
        "total_biens": total_biens,
        "solde_global": solde_global
    }
    return render(request, "rapports/rapport_global.html", context)

def rapport_cahier(request, cahier_id):
    cahier = get_object_or_404(Cahier, pk=cahier_id)

    avances = AvanceArgent.objects.filter(cahier=cahier)
    biens = EchangeBiens.objects.filter(cahier=cahier)

    total_avances = sum(avance.montant for avance in avances)
    total_biens = sum(bien.prix for bien in biens)
    solde = total_avances - total_biens

    moyenne_avances = total_avances / len(avances) if avances else 0
    moyenne_biens = total_biens / len(biens) if biens else 0
    total_transactions = len(avances) + len(biens)

    context = {
        "cahier": cahier,
        "total_avances": total_avances,
        "total_biens": total_biens,
        "solde": solde,
        "statut_solde": cahier.statut_solde,
        "moyenne_avances": moyenne_avances,
        "moyenne_biens": moyenne_biens,
        "total_transactions": total_transactions,
        "avances": avances,
        "biens": biens,
    }
    return render(request, "rapports/rapport_cahier.html", context)