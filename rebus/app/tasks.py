# -*- coding: utf8 -*-
from __future__ import absolute_import
from celery import shared_task
from app.investments import InvestmentLogic 
from app.models import Investment
import conekta


@shared_task
def cobro():
	# invest = Investment.objects.get(request.user)
	# card = CreditCard.objects.get(request.user)
	# token = card.token
	cobro = 10000
	print InvestmentLogic.get_stocks_to_buy(7)
	print InvestmentLogic.buy_stock(cobro,4)
	conekta.api_key = 'key_CAniAetz1nboWvXz4MwCHEQ'

	charge = conekta.Charge.create({
	    "currency":"MXN",
	    "amount": cobro,
	    "description":"Stogies",
	    "reference_id":"9839-wolf_pack",
	    "card": "tok_RzMQuwwJvEK7VYmQa"
	})
	print "Compraré"

@shared_task
def compra():
    print "Compraré :D"