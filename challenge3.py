# single-byte xor cipher
from binascii import unhexlify
hexed = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
unHexed = unhexlify(hexed)
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# generate a dict of possible answers and their decryption keys
tableOfPossibleAnswers = {}
for code in range(256):
    possibleAnswer = ''.join(chr(byte ^ code) for byte in unHexed)
    if possibleAnswer.isprintable():
        tableOfPossibleAnswers[code] = possibleAnswer

# weight the answers using a simple english alphabet list
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