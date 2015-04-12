from app import models as appModels
from django import forms


class InvestmentForm(forms.ModelForm):
	def save(self, user=None):
		self.instance.user = user
		super(InvestmentForm, self).save()

	class Meta:
		model = appModels.Invenstment
		fields = ['monthly_payment', 'objective', 'payment_mode']

class CreditCardForm(forms.ModelForm):
	class Meta:
		model = appModels.creditCard
		fields = ['token']

