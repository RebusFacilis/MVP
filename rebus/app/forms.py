# -*- encoding:utf-8 -*-
from app import models as appModels
from django import forms

TIEMPO = (
	(6, '6 meses'),
	(12, '12 meses'),
	(18, '18 meses'),
	(24, '24 meses')
)

class InvestmentInfoForm(forms.Form):
	meta = forms.FloatField(help_text='¿Cuál es tu meta?')
	inversion = forms.FloatField()
	tiempo = forms.ChoiceField(choices=TIEMPO)

class InvestmentForm(forms.ModelForm):
	def save(self, user=None):
		self.instance.user = user
		super(InvestmentForm, self).save()

	class Meta:
		model = appModels.Investment
		fields = ['monthly_payment', 'goal', 'payment_mode']

class CreditCardForm(forms.ModelForm):
	class Meta:
		model = appModels.CreditCard
		fields = ['token']
