from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def empList(request):
    employee = Employee.objects.all()
    return render(request, 'list.html', {'employee':employee})

def empCreate(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'form.html', {'form':form})

def empUpdate(request, pk):
    emp = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=emp)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'form.html', {'form':form})

def empDelete(request, pk):
    emp = Employee.objects.get(id=pk)
    emp.delete()
    return redirect('/')

