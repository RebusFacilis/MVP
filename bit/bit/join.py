import json

def main():

    ## Shit!
    financial = open('outputs/financial.txt').read()
    valuation = open('outputs/valuation.txt').read()

    financialInput = financial.split('<<<>>>')
    valuationInput = valuation.split('<<<>>>')

    # Refactoring...
    financial = []
    for tricker in financialInput:
        try:
            financial.append(json.loads(tricker))
        except:
            pass

    valuation = []
    for tricker in valuationInput:
        try:
            valuation.append(json.loads(tricker))
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

    import pprint
    pprint.pprint(mix)

main()