from app import forms as f
import math

class InvestmentLogic(object):
	@staticmethod
	def buy_stock():
		pass

	
def get_time(goal, monthly_payment, payment_mode):
    necessary = goal / monthly_payment
    cetes = .00302
    rebus = .2435

    if necessary > payment_mode:
    	return None, None

    time_cetes = math.log(1+(goal*cetes)/monthly_payment)/math.log(1+cetes)
    time_cetes = math.ceil(time_cetes)
    time_rebus = math.log(1+(goal*rebus)/monthly_payment)/math.log(1+rebus)
    time_rebus = math.ceil(time_rebus)

    return time_cetes, time_rebus

