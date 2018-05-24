from pybaseconv import Converter, BASE

dec2hex_converter = Converter(BASE.DEC, BASE.HEX)
print(dec2hex_converter.convert('738653'))  # returns b455d

dec2bitcoin_converter = Converter(BASE.DEC, BASE.BITCOIN_BASE_58)
print(dec2bitcoin_converter.convert('292251'))  # returns 2Vsp

dec2custom_base_converter = Converter(BASE.DEC, '*&@#$')
print(dec2custom_base_converter.convert('539'))  # returns $&@$

bin2dec_converter = Converter(BASE.BIN, BASE.DEC)
# raises exception because 11112 is not a binary number
print(bin2dec_converter.convert('11112'))
