from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from .models import global_report, camion_performance

class ReportsAdminSite(admin.AdminSite):
    site_header = "Tableau de Bord - Rapports et Statistiques"
    site_title = "Administration des Rapports"
    index_title = "Rapports et Statistiques de l'Entreprise"

    def get_urls(self):
        # On ajoute une URL personnalisée pour accéder au tableau de bord
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name="dashboard"),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        """
        Vue qui génère le tableau de bord à partir des données existantes.
        """
        context = dict(
            self.each_context(request),
            global_stats=global_report(),
            camion_stats=camion_performance(),
        )
        return TemplateResponse(request, "rapports/dashboard.html", context)

# Instanciation du site d'administration personnalisé pour les rapports
reports_admin_site = ReportsAdminSite(name="reports_admin")
