from django.shortcuts import render

def home(request):
    return render(request, 'systeme_gestion_personnel/home.html')
