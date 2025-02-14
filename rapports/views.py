from django.shortcuts import render
from .reports import global_report, camion_performance, employee_report

def dashboard(request):
    context = {
        'global_stats': global_report(),
        'camion_stats': camion_performance(),
        'employee_stats': employee_report(),
    }
    return render(request, 'rapports/dashboard.html', context)
