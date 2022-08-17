from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(reuqest):
    return render(reuqest,'index.html')

def login(reuqest):
    return render(reuqest,'login.html')

def signup(request):
    if request.method == 'GET':

        form= UserCreationForm()
        context = {
            'form' : form
        }
        return render(request,'signup.html',context=context)

    else:
        print(request.POST)
        form= UserCreationForm(request.POST)
        context = {'form' : form}
        if form.is_valid():
            
            user = form.save()
            print(user)
            if user is not None:
                return redirect('home')

        else:
            #return HttpResponse('Invalid')
            return render(request,'signup.html',context=context)
        


