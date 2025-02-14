from django.contrib import admin
from django.urls import path, include
from systeme_gestion_personnel import views  # Assurez-vous d'importer vos vues

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Route pour la page d'accueil
    path('rapports/', include('rapports.urls', namespace='reports_admin')),
    path('camions/', include('camions.urls', namespace='camions')),
    path('cahier_clients/', include('cahier_clients.urls', namespace='cahier_clients')),
    path('employes/', include('employes.urls', namespace='employes')),
]
