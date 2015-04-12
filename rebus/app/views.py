from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import View
from app import forms as f

class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('user'))
        else:
            messages.error(request, u'Usuario/Password incorrectos')
            return redirect(reverse('login'))

class UserView(View):
    def get(self, request):
        form = f.InvestmentForm()
        print form
        return render(request, 'index.html', {'form': form})

    def post(self,request):
        form = f.InvestmentForm(request.POST)
        if form.is_valid():
            form.save(user = request.user)
            return redirect('dashboard-user')
        else:
            return render(request, 'index.html', {'form': form})
    

def dashboard_user(request):
    return render(request, 'userData.html', locals())


