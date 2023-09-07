from django.shortcuts import render,redirect
from .models import StudentsData
def homepage(request):
    students=StudentsData.objects.all()
    return render(request,'homepage.html',{'students':students})

def add_student(request):
    if request.method=='GET':
        return render(request,'add_student.html')
    else:
        StudentsData(
            first_name=request.POST.get('fname'),
            last_name=request.POST.get('lname'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            course=request.POST.get('course'),
            fee=request.POST.get('fee'),
            dob=request.POST.get('dob'),
            location=request.POST.get('location'),
        ).save()
        return redirect('homepage')

def student_data(request,id):
    student=StudentsData.objects.get(id=id)
    return render(request,'student_data.html',{'student':student})
# Create your views here.
