from django.urls import path
from . import views

app_name = "camions"  # Nom d'espace de l'application

urlpatterns = [
    # Page d'accueil ou index
    path('', views.camion_list, name='index'),

    # Gestion des camions
    path('camions/', views.camion_list, name='camion_list'),
    path('camions/ajouter/', views.camion_create, name='camion_create'),
    path('camions/detail/<int:pk>/', views.camion_detail, name='camion_detail'),
    path('camions/modifier/<int:pk>/', views.camion_edit, name='camion_edit'),
    path('camions/supprimer/<int:pk>/', views.camion_delete, name='camion_delete'),

    # Gestion des trajets
    path('trajets/', views.trajet_list, name='trajet_list'),
    path('trajets/ajouter/', views.trajet_create, name='trajet_create'),
    path('trajets/detail/<int:pk>/', views.trajet_detail, name='trajet_detail'),
    path('trajets/modifier/<int:pk>/', views.trajet_edit, name='trajet_edit'),
    path('trajets/supprimer/<int:pk>/', views.trajet_delete, name='trajet_delete'),

    # Gestion des entretiens
    path('entretiens/', views.entretien_list, name='entretien_list'),
    path('entretiens/ajouter/', views.entretien_create, name='entretien_create'),
    path('entretiens/supprimer/<int:pk>/', views.entretien_delete, name='entretien_delete'),

    # Gestion des dépenses
    path('depenses/', views.depense_list, name='depense_list'),
    path('depenses/ajouter/', views.depense_create, name='depense_create'),
    path('depenses/modifier/<int:pk>/', views.depense_update, name='depense_update'),
    path('depenses/supprimer/<int:pk>/', views.depense_delete, name='depense_delete'),

    # Gestion des revenus
    path('revenus/', views.revenu_list, name='revenu_list'),
    path('revenus/ajouter/', views.revenu_create, name='revenu_create'),
    path('revenus/supprimer/<int:pk>/', views.revenu_delete, name='revenu_delete'),

    # Route pour le rapport global (dashboard)
    path('rapport/dashboard/', views.rapport_dashboard, name='rapport_dashboard'),
    
    # Route pour le rapport des camions
    path('rapport/rapport_camion/', views.rapport_camion, name='rapport_camion'),
]
