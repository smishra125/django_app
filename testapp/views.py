from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee
# Create your views here.

def greeting(request):
    s="<h1>Hello and Welcome to first View of testapp</h1><p>This is landing page</p>"
    return HttpResponse(s)

def showContact(request):
    s="<h1>Contact Page</h1>"
    s+="<p>Website: mysirg.com</p>"
    s+="<p>Mobile: 9009009001</p>"
    s+="<p>Email: something@gmail.com</p>"
    return HttpResponse(s)

def about(request):
    s="<h1>This is an about page</h1>"
    return HttpResponse(s)

def employee_info_view(request):
    employees=Employee.objects.all()
    data = {'employees':employees}
    res = render(request, 'test/employee.html', data)
    return res