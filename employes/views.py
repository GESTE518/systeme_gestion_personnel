from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Employe
from .forms import EmployeForm

# Liste des employés
def employe_list(request):
    employes = Employe.objects.all()
    return render(request, 'employes/employe_list.html', {'employes': employes})

# Détails d'un employé
def employe_detail(request, pk):
    employe = get_object_or_404(Employe, pk=pk)
    return render(request, 'employes/employe_detail.html', {'employe': employe})

# Ajouter un nouvel employé
def employe_create(request):
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employes:employe_list')
    else:
        form = EmployeForm()
    return render(request, 'employes/employe_form.html', {'form': form})

# Modifier un employé existant
def employe_edit(request, pk):
    employe = get_object_or_404(Employe, pk=pk)
    if request.method == 'POST':
        form = EmployeForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()
            return redirect('employes:employe_list')
    else:
        form = EmployeForm(instance=employe)
    return render(request, 'employes/employe_form.html', {'form': form})

# Supprimer un employé
def employe_delete(request, pk):
    employe = get_object_or_404(Employe, pk=pk)
    if request.method == 'POST':
        employe.delete()
        return redirect('employes:employe_list')
    return render(request, 'employes/employe_confirm_delete.html', {'employe': employe})
