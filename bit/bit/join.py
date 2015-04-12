import json
from sort import sort_by_indicator, rank_to_dict, mix_ranks, to_mix
import pprint, operator

def discart_pe(key):
    return None if key <= 5 else key

def main():

    ## Shit!
    financial = open('outputs/financial.txt').read()
    valuation = open('outputs/valuation.txt').read()

    financialInput = financial.split('<<<>>>')
    valuationInput = valuation.split('<<<>>>')

    # Refactoring...
    financial = []
    for ticker in financialInput:
        try:
            financial.append(json.loads(ticker))
        except:
            pass

    valuation = []
    for ticker in valuationInput:
        try:
            valuation.append(json.loads(ticker))
        except:
            pass

    ## To dict
    mix = {}
    for fin in financial:
        for k, v in fin.items():
            mix[k] = v

    valuationMix = {}
    for val in valuation:
        for k, v in val.items():
            valuationMix[k] = v

    ## Mixing
    for k, v in mix.items():
        if k in valuationMix:
            mix[k].update(valuationMix[k])

    mix_pe = sort_by_indicator(mix, key='P/E', filters=[discart_pe])
    mix_roi = sort_by_indicator(mix, key='ROI', reverse=True)

    rank_pe = rank_to_dict(mix_pe)
    rank_roi = rank_to_dict(mix_roi)

    mixed_rank = mix_ranks(rank_pe, rank_roi)
    mixed_rank_ordered = sorted(mixed_rank.items(), key=operator.itemgetter(1))
    mixed_rank_ordered = mixed_rank_ordered[:30]

    mixed = to_mix(mix, mixed_rank_ordered)
    price_mix = sort_by_indicator(mixed, 'Price')
    pprint.pprint(price_mix)


main()