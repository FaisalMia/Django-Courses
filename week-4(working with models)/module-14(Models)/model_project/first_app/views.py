from django.shortcuts import render,redirect
from . import models

# Create your views here.
def home(request):
    # return render(request,'home.html')
    student = models.Student.objects.all()
    # print(student)
    return render(request,'home.html',{'data' : student})

def delete_student(request,roll):
    std = models.Student.objects.get(pk=roll).delete()
    # print(std)
    # student = models.Student.objects.all()
    # return render(request,'home.html',{'data' : student})
    return redirect("homepage")
    