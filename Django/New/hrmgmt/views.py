from django.shortcuts import render

from .models import Employee

# Create your views here.
def index(request):
    order_by = request.GET.get('order_by', 'id')
    employees = Employee.objects.order_by(order_by).all()
    context = {'employees': employees}
    return render(request, 'index.html', context)
