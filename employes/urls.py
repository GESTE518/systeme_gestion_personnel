from django.urls import path
from . import views

app_name = 'employes'

urlpatterns = [
    path('', views.employe_list, name='employe_list'),  # Accueil de la liste des employés
    path('detail/<int:pk>/', views.employe_detail, name='employe_detail'),
    path('ajouter/', views.employe_create, name='employe_create'),
    path('modifier/<int:pk>/', views.employe_edit, name='employe_edit'),
    path('supprimer/<int:pk>/', views.employe_delete, name='employe_delete'),
    path('index/', views.employe_list, name='index'),  # Ajout de la vue 'index' pour la page d'accueil
]
