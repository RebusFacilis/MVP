import json

def main():

    ## Shit!
    financial = open('html/financial.txt').read()
    valuation = open('html/valuation.txt').read()

    _output1 = financial.split('<<<>>>')
    _output2 = valuation.split('<<<>>>')

    # Refactoring...
    financial = []
    for tricker in _output1:
        try:
            financial.append(json.loads(tricker))
        except:
            pass

    valuation = []
    for tricker in _output2:
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