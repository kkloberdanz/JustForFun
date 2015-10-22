"""
Programmer  : Kyle Kloberdanz
Date Created: 9 Oct 2015
Description : Input can either be an integer or floating 
              point number
              Returns a string in scientific notation 
              
Warning: Overflow occurs for FLOATS with exponents greater than 14
"""
def sciNotation( dec ):

    # For positive integers
    if (dec > 0) and (int(dec) == dec):
        dec = int(dec)
        mantissa = ""
        while dec >= 10:
            mantissa = str(dec%10) + mantissa 
            dec = dec // 10
        return str(dec)+"." + mantissa + "x10^" + str(len(mantissa))

    # For negative integers
    elif (dec < 0) and (int(dec) == dec):
        dec = int(abs(dec))
        mantissa = ""
        while dec >= 10:
            mantissa = str(dec%10) + mantissa 
            dec = dec // 10
        return "-"+str(dec)+"."+mantissa+"x10^"+str(len(mantissa))

    # For positive floats
    elif (dec >= 1) and (int(dec) != dec):
        # Gets the numbers after the deciaml
        mantissa = str(dec)[str(dec).index(".")+1:]

        startingLengthOfMantissa = len(mantissa)
        dec = int(dec)
        while dec >= 10:
            mantissa = str(dec%10) + mantissa 
            dec = dec // 10
        return str(dec)+"." + mantissa + "x10^" + str(len(mantissa) - startingLengthOfMantissa)

    # For negative floats
    elif (dec <= -1) and (int(dec) != dec):
        dec = abs(dec)

        # Gets the numbers after the deciaml
        mantissa = str(dec)[str(dec).index(".")+1:]

        startingLengthOfMantissa = len(mantissa)
        dec = int(dec)
        while dec >= 10:
            mantissa = str(dec%10) + mantissa 
            dec = dec // 10
        return "-"+str(dec)+"."+ mantissa + "x10^" + str(len(mantissa) - startingLengthOfMantissa)

    # Floats abs < 1
    elif (abs(dec) < 1) and (dec > 0):
        dec = str(dec)
        mantissa = dec[ dec.index("."): ]
        exp = str(len(mantissa) - 1)
        dec = dec[2:]
        while dec[0] == '0':
            dec = dec[1:]
        dec = dec[0]
        mantissa = mantissa[1:]
        while mantissa[0] == '0':
            mantissa = mantissa[1:]
        mantissa = mantissa[1:]
        return dec + '.' + mantissa + "x10^-" + exp
    elif (abs(dec) < 1) and (dec < 0):
        return dec
    # For zero
    elif dec == 0:
        return 0

    # This shouldn't happen
    else:
        return "This feature has not yet been built"
    
'''
sci = sciNotation(123456789123456781234456669)
print(sci)

sci = sciNotation(-1234)
print(sci)

sci = sciNotation(1234567891789123456789.123456789)
print(sci)

sci = sciNotation(-123456789116789.123456789)
print(sci)

sci = sciNotation(.12345)
print(sci)

sci = sciNotation(-.12345)
print(sci)

sci = sciNotation(-12345.6789)
print(sci)

print(sciNotation(0.9))
print(sciNotation(0.0009003450))
print(sciNotation(-0.00009))
'''
