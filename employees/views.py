from django.shortcuts import render
from .models import Department

def department_tree_view(request):
    departments = Department.objects.filter(parent__isnull=True).prefetch_related('children', 'employees')
    return render(request, 'index.html', {'departments': departments})
