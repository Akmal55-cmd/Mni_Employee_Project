from django.shortcuts import render, get_object_or_404,redirect
from .models import Employee
from .models import Department
from .models import Company

# Create your views here.
def display(request):
    data=Employee.objects.all()
    return render(request,"empdata.html",{'employeedata': data})


def addEmpData(request):
    dept_data = Department.objects.all()
    comp_data = Company.objects.all()
    name = request.POST.get('name')
    email = request.POST.get('email')
    age = request.POST.get('age')
    salary = request.POST.get('salary')
    department_id = request.POST.get('department')
    company_id = request.POST.get('company')
    address = request.POST.get('address')
    
    # print(name,email,age,salary,department,company,address)
    if request.method=='POST':
        ee = Employee(name=name, age=age, email=email, salary=salary, department_id=department_id, company_id=company_id, address=address,)
        ee.save()
        msg = "Data Added Successfully"
        return render(request, "form.html", {'msg': msg})

    return render(request, "form.html", context={'dept_data': dept_data, 'comp_data': comp_data})


def updateEmpData(request, id):
    dept_data = Department.objects.all()
    comp_data = Company.objects.all()
    emp = get_object_or_404(Employee, id=id)
    print('--->', emp)


    if request.method=='POST':
        emp.name = request.POST.get('name')
        emp.email = request.POST.get('email')
        emp.age = request.POST.get('age')
        emp.salary = request.POST.get('salary')
        # emp.department_id = request.POST.get('department')
        # emp.company_id = request.POST.get('company')
        emp.address = request.POST.get('address')
        emp.save()
        

    return render(request, 'editform.html', {'emp':emp, 'dept_data': dept_data, 'comp_data': comp_data})

    

def deleteEmpData(Request,id):
    emp = get_object_or_404(Employee,id=id)
    emp.delete()
    return redirect('empdata')