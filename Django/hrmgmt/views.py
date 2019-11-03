from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Employee
from django.contrib.auth import authenticate, login


@login_required
def index(request):
    order_by = request.GET.get('order_by', 'id')
    employees = Employee.objects.order_by(order_by).all()[:100]
    context = {'employees': employees}
    return render(request, 'index.html', context)
