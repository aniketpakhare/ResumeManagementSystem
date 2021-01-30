from django.shortcuts import render
from rmsapp.forms import RegistrationForm


def showIndex(request):
    return render(request,"rmsapp_templates/main.html")


def registration(request):
    rf = RegistrationForm(request.POST)
    if request.method == 'POST':
        pass
    else:
        return render(request,'rmsapp_templates/registration.html',{"form":rf})