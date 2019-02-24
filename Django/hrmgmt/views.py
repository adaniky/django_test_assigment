from django.shortcuts import render

from .models import Employee

# Create your views here.
def index(request):
    employees = Employee.objects.order_by('id').all()
    context = {'employees': employees}
    return render(request, 'index.html', context)
