from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as loginuser
# Create your views here.

def home(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'GET':

        form=  AuthenticationForm()
        context = {'form': form}
        return render(request,'login.html', context= context)
    
    else:
        form =AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password= password)
            print('Authenicated', user)
            if user is not None:
                loginuser(request, user)
                return redirect('home')

        else:
            context = {'form': form}
            return render(request,'login.html', context= context)


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
                return redirect('login')

        else:
            #return HttpResponse('Invalid')
            return render(request,'signup.html',context=context)
        
