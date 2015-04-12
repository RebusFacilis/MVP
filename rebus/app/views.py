from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import View
from app.investments import InvestmentLogic
from app.models import Investment, CreditCard
from app import forms as f
from django.http import Http404
from datetime import datetime, timedelta
import conekta

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

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(reverse('user'))
        super(Login, self).dispatch(request, *args, **kwargs)

class UserInvestmentView(View):
    def get(self, request):
        form = f.InvestmentInfoForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = f.InvestmentInfoForm(request.POST)
        if not form.is_valid():
            return render(request, 'index.html', {'form': form})

        meta = form.cleaned_data['meta']
        inversion = form.cleaned_data['inversion']
        tiempo = form.cleaned_data['tiempo']        
        time_cetes, time_rebus = InvestmentLogic.get_time(meta, inversion, tiempo)
        print int(time_rebus)
        print int(time_cetes)

        sin_inversion = int(meta) / int(inversion)
        pcetes = (int(time_cetes) * 100) / int(sin_inversion)
        prebus = (int(time_rebus) * 100) / int(sin_inversion)

        return render(request, 'user_dashboard.html', {
            'meta': meta,
            'inversion': inversion,
            'tiempo': tiempo,
            'time_cetes': time_cetes,
            'time_rebus': time_rebus,
            'portfolio': [],
            'pcetes': pcetes,
            'prebus': prebus,
            'sin_inversion': sin_inversion,
        })
class UserInvestmentConfirmationView(View):
    def post(self, request):
        form = f.InvestmentInfoForm(request.POST)
        if not form.is_valid():
            raise Http404

        meta = form.cleaned_data['meta']
        inversion = form.cleaned_data['inversion']
        tiempo = form.cleaned_data['tiempo']
        o, months = InvestmentLogic.get_time(meta, inversion, tiempo)

        end_date = timedelta(months*365/12)
        Investment.objects.create(
            monthly_payment=inversion,
            goal=meta, start_date=datetime.now(),
            end_date=datetime.now() + end_date, 
            user=request.user)

        return redirect(reverse('dashboard-user'))


def dashboard_user(request):
    return render(request, 'chart.html')

def cardform(request):
    return render(request, 'pagos.html')

def token_credit_card(request):
    token = request.POST['token_id']
    try:
      customer = conekta.Customer.create({
        "name": request.POST['name'],
        "email": "lews.therin@gmail.com",
        "phone": "55-5555-5555",
        "cards": request.POST['token_id'],
    # request.form["conektaTokenId"], request.params["conektaTokenId"], "tok_a4Ff0dD2xYZZq82d9"
      })
    except conekta.ConektaError as e:
        print e.message 
    # el cliente no pudo ser creado
    CreditCard.objects.create(token=token, user=request.user)
    return redirect(reverse('cards'))
