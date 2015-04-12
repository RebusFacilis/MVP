import json
from sort import sort_by_indicator, rank_to_dict, mix_ranks, to_mix
import pprint, operator
import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def discart_pe(key):
    return None if key <= 5 else key

def main():

    ## Shit!
    financialPath = os.path.join(BASE, 'outputs/financial.txt')
    valuationPath = os.path.join(BASE, 'outputs/valuation.txt')
    financial = open(financialPath).read()
    valuation = open(valuationPath).read()

    financialInput = financial.split('<<<>>>')
    valuationInput = valuation.split('<<<>>>')

    # Refactoring...
    financial = []
    for ticker in financialInput:
        if not ticker:  continue
        try:
            financial.append(json.loads(ticker))
        except Exception as e:
            raise e

    valuation = []
    for ticker in valuationInput:
        if not ticker:  continue
        try:
            valuation.append(json.loads(ticker))
        except Exception as e:
            raise e

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

    path = os.path.join(BASE, 'outputs/final.txt')
    f = open(path, 'w')
    f.write(json.dumps(price_mix))
    f.close()
    # pprint.pprint(price_mix)


main()