import math
	
tickers = [
	["LFVN", 0.69], 
	["SMT", 1.24], 
	["RVSB", 4.49], 
	["UCFC", 5.48], 
	["HGT", 5.79], 
	["MLP", 6.06], 
	["DOM", 6.22], 
	["CWBC", 6.62], 
	["GAME", 6.85], 
	["PBT", 8.61], 
	["TZOO", 9.57], 
	["MARPS", 12.0], 
	["SJT", 12.02], 
	["FONR", 12.31], 
	["NRT", 12.67], 
	["BFIN", 12.87], 
	["MSB", 15.8], 
	["KING", 16.9], 
	["ALDW", 18.62], 
	["CRT", 19.62], 
	["BFR", 20.77], 
	["ANCB", 21.82], 
	["OCIR", 22.06], 
	["MTR", 22.31], 
	["PPC", 23.29], 
	["GGAL", 23.54], 
	["ARLP", 33.75], 
	["SBR", 39.9], 
	["BMA", 57.1], 
	["SAFM", 79.05]
]

class InvestmentLogic(object):
	@staticmethod
	def get_stocks_to_buy(time):
		stocks = len(tickers)
		to_buy = stocks / time
		plan = []
		suma = 0
		while suma < stocks:
			suma += to_buy
			plan.append(to_buy)
		suma -= to_buy
		if not suma == stocks:
			plan.append(stocks - suma)
		return plan

	@staticmethod
	def get_time(goal, monthly_payment, payment_mode):
	    necessary = goal / monthly_payment
	    cetes = .0302
	    rebus = .2435

	    if necessary > payment_mode:
	    	return None, None

	    time_cetes = math.log(1+(goal*cetes)/monthly_payment)/math.log(1+cetes)
	    time_cetes = math.ceil(time_cetes)
	    time_rebus = math.log(1+(goal*rebus)/monthly_payment)/math.log(1+rebus)
	    time_rebus = math.ceil(time_rebus)

	    return time_cetes, time_rebus

	@staticmethod
	def buy_stock(budget, stocks):
		stocksList = tickers[:stocks]
		remaining = 0
		budgetXstock = budget / stocks
		stocksBought = {}
		for stockItem in stocksList:
			stocksBought[stockItem[0]] = 0

		# while remaining:
		for stock in stocksList:
			price = stock[1]
			budgetAvailable = budgetXstock
			while budgetAvailable > price:
				stocksBought[stock[0]] += 1
				budgetAvailable -= price
			remaining += budgetAvailable

		print stocksBought, remaining


# print InvestmentLogic.buy_stock(10000, 4)
# print InvestmentLogic.get_stocks_to_buy(7)
