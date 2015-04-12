def format_key(item):
	key = item
	key = key.replace('%', '').replace(',', '')

	if len(key) is 1 and key == '-':
		key = 0

	try:
		key = float(key)
	except Exception as e:
		key = 0

	return key

def to_mix(master_mix, inputList):
	mix = {}
	for item in inputList:
		ticker = item[0]
		mix[ticker] = master_mix[ticker]

	return mix

def mix_ranks(rank_one, rank_two):
	mixed_rank = {}
	for k, v in rank_one.items():
		if k in rank_two:
			# print k, v, rank_two[k]
			mixed_rank[k] = rank_one[k] + rank_two[k]
	return mixed_rank

def rank_to_dict(rank):
	ranking = {}
	for index, ticker in enumerate(rank):
		ticker_name = ticker[0]
		ticker_ranking = ticker[1]
		ranking[ticker_name] = index
	return ranking 

def sort_by_indicator(mix, key='ROI', reverse=False, filters=[]):
	to_sort = []
	for ticker, indi in mix.items():
		formated_key = format_key(indi[key])

		for f in filters:
			formated_key = f(formated_key)

		if formated_key:
			to_sort.append((ticker, formated_key))

	to_sort = sorted(to_sort, key=lambda x: x[1], reverse=reverse)

	return to_sort
