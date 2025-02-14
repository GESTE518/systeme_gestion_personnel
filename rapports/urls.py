from django.urls import path
from . import views  # Assure-toi d'importer les vues

app_name = 'reports_admin'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),  # Assure-toi que le nom 'dashboard' est bien ici
]
