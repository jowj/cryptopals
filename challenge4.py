import requests
from binascii import unhexlify

# get the list of strings (each string is 60 characters)
request = requests.get('https://cryptopals.com/static/challenge-data/4.txt')
requestArray = request.text.splitlines()

# here's the code used in challenge 3, which is said to be useful
def xor_SingleByte(hexed):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    unHexed = unhexlify(hexed)
    # generate a dict of possible answers and their decryption keys
    
    tableOfPossibleAnswers = {}
    for code in range(256):
        possibleAnswer = ''.join(chr(byte ^ code) for byte in unHexed)
        if possibleAnswer.isprintable():
            tableOfPossibleAnswers[code] = possibleAnswer

    # weight the answers using a simple english alphabet list
    if tableOfPossibleAnswers:
        weightedCodes = {}
        for key,value in tableOfPossibleAnswers.items():
            weightedCodes[value] = 0
            for letter in alphabet:
                if letter in value:
                    weightedCodes[value] += 1

        # find the highest value and return it and its corresponding key
        maxValue = max(weightedCodes.values())
        answerValue = []
        for key in weightedCodes:
            if weightedCodes[key] == maxValue:
                answerValue = key
        
        # now i need to use that to key into the original tableOfPossibleAnswers to return the answer and the decryption key.
        for key,value in tableOfPossibleAnswers.items():
            if tableOfPossibleAnswers[key] == answerValue:
                print(key, tableOfPossibleAnswers[key])


for string in requestArray:
    xor_SingleByte(string)