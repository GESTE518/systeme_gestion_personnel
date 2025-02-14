from django.urls import path
from . import views

app_name = 'cahier_clients'

urlpatterns = [
    path('', views.cahier_list, name='index'),
    path('cahier/ajouter/', views.cahier_create, name='cahier_create'),
    path('cahier/<int:pk>/', views.cahier_detail, name='cahier_detail'),

    # Gestion de la modification et suppression des cahiers
    path('cahier/<int:pk>/edit/', views.cahier_edit, name='cahier_edit'),
    path('cahier/<int:pk>/delete/', views.cahier_delete, name='cahier_delete'),

    # Gestion des Avances d'Argent
    path('cahier/<int:cahier_pk>/avance/', views.avance_argent_create, name='avance_argent_create'),
    path('avance/<int:pk>/edit/', views.avance_argent_edit, name='avance_argent_edit'),
    path('avance/<int:pk>/delete/', views.avance_argent_delete, name='avance_argent_delete'),

    # Gestion des rapports cahier
    path('rapport/global/', views.rapport_global, name='rapport_global'),
    path('rapport/cahier/<int:cahier_id>/', views.rapport_cahier, name='rapport_cahier'),  # ✅ Correction ici

    # Gestion des Échanges de Biens
    path('cahier/<int:cahier_pk>/echange/', views.echange_biens_create, name='echange_biens_create'),
    path('echange/<int:pk>/edit/', views.echange_biens_edit, name='echange_biens_edit'),
    path('echange/<int:pk>/delete/', views.echange_biens_delete, name='echange_biens_delete'),
]
