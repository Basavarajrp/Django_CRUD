from django.shortcuts import render,redirect
from .forms import EmployeeForm
from App.models import Employee 

# Create your views here.
def emp_list(request):
    d = Employee.objects.all()
    return render(request,"App/emp_list.html",{
        'employee':d
    })

def emp_form(request,id=0):
     
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request,"App/emp_form.html",{'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance = employee)
        
        if form.is_valid():
            form.save()
        return redirect('/emp/list')    

def emp_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/emp/list')