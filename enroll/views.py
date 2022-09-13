from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration


# Create your views here.
def showformdata(request):
    if request.method =='POST':
        fm=StudentRegistration(request.Post)
        if fm.is_valid():
            print("validate")
            print("name:",fm.cleaned_data["name"])
            print("roll:", fm.cleaned_data[" roll"])
            print("price:", fm.cleaned_data["price"])
            print("float:", fm.cleaned_data["float"])
            print("Agree:", fm.cleaned_data[" i Agree"])

        else:
            fm=StudentRegistration()

        return render(request,'enroll/user_registration.html',{'form':fm})