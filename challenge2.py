
def fixedXor(arg1, arg2):
    input1 = int(arg1, 16)
    input2 = int(arg2, 16)

    hexData = (hex(input1 ^ input2))
    return hexData[2:]

print(fixedXor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"))