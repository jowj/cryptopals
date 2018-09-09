from binascii import unhexlify, b2a_base64
import base64

# Use the binascii.unhexlify() function to convert from a hex string to bytes. Then use the binascii.b2a_base64() function to convert that to Base64:
hexstring = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
bytesThing = bytes.fromhex(hexstring)

result = base64.b64encode(bytesThing)
utfresult = result.decode("utf-8")

print(utfresult)