from binascii import unhexlify

# see what each value is unhexlified:
test = bytearray.fromhex("1c0111001f010100061a024b53535009181c").decode()
test2 = bytearray.fromhex("686974207468652062756c6c277320657965").decode()
print(test)
print(test2)

# if converting from strings, you must convert characters to integers and XOR those instead, and then...unconvert them?
# example with XORing integers
input1 = 12345
input2 = 67890
xored1 = input1 ^ input2
print(xored1)

# now prove that worked

print(input1 ^ xored1) # should be = to input2

# now i need to convert strings to integers
text = "suck myass BITCH"
numArray = []
for letter in text:
    number = ord(letter)
    numArray.append(number)

print(numArray)

# ok now convert that array of ints back to strings
letterArray = []
for number in numArray:
    letter = chr(number)
    letterArray.append(letter)

print(letterArray)

# OK DOPE now turn it into a function

def xor_TwoEqualLengthBuffers(arg1, arg2):
    arg1value = bytearray.fromhex(arg1).decode()
    arg2value = bytearray.fromhex(arg2).decode()

    numArray1 = []
    for letter in arg1value:
        number1 = ord(letter)
        numArray1.append(number1)

    int1 = int(''.join(str(i) for i in numArray1))


    numArray2 = []
    for letter in arg2value:
        number2 = ord(letter)
        numArray2.append(number2)
    
    int2 = int(''.join(str(i) for i in numArray2))


    xoredValue = int1 ^ int2


xor_TwoEqualLengthBuffers("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")