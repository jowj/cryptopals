import requests
from binascii import unhexlify


# convert that to int, since we're gonna be xoring it
def hexToIntConversion(hexString):
    '''use like "hexToIntConversion(given)"
    '''
    converedBytes = unhexlify(hexString)
    return converedBytes


# xor new int with all possible ascii codes
def xorIntAgainstAllAsciiCodes(convertedBytes):
    '''use like "print(xorIntAgainstAllAsciiCodes(hexToIntConversion(given)))"
    '''
    possibleAnswers = {}
    for possibleKey in range(256):
        possibleAnswers[possibleKey] = ''.join(chr(byte ^ possibleKey) for byte in convertedBytes)
    
    return possibleAnswers

# ok great, you have the data you need, now you have to *weigh* the data you have
def weighPossibleAnswers(possibleAnswers):
    freqs = {
        'a': 0.0651738, 'b': 0.0124248,'c': 0.0217339,
        'd': 0.0349835,'e': 0.1041442,'f': 0.0197881,
        'g': 0.0158610,'h': 0.0492888,'i': 0.0558094,
        'j': 0.0009033,'k': 0.0050529,'l': 0.0331490,
        'm': 0.0202124,'n': 0.0564513,'o': 0.0596302,
        'p': 0.0137645,'q': 0.0008606,'r': 0.0497563,
        's': 0.0515760,'t': 0.0729357,'u': 0.0225134,
        'v': 0.0082903,'w': 0.0171272,'x': 0.0013692,
        'y': 0.0145984,'z': 0.0007836,' ': 0.1918182
    }
    
    scoredAnswers = {}

    for answer in possibleAnswers.values():
        scoredAnswers[answer] = 0
        for letter in answer:
            if letter in freqs.keys():
                scoredAnswers[answer] += freqs[letter]
    
    return scoredAnswers

def rateWeighedAnswers(scoredAnswers):
    mostLikelyAnswer = max(scoredAnswers.values())
    ratedAndWeighedAnswers = {}

    for key,value in scoredAnswers.items():
        if value == mostLikelyAnswer:
            ratedAndWeighedAnswers[key] = value

    return ratedAndWeighedAnswers


def main():
    # what do we start with?
    # get the list of strings (each string is 60 characters)
    request = requests.get('https://cryptopals.com/static/challenge-data/4.txt')
    requestArray = request.text.splitlines()

    ratedDataTable = {}
    for eachRequest in requestArray:
        byteConversion = hexToIntConversion(eachRequest)
        xoredData = xorIntAgainstAllAsciiCodes(byteConversion)
        ratedData = rateWeighedAnswers(weighPossibleAnswers(xoredData))

        ratedDataTable.update(ratedData)
    
    print(rateWeighedAnswers(ratedDataTable))

if __name__ == "__main__":
    main()
