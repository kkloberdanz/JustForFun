# Programmer: Kyle Kloberdanz

def myFunction(x):
    return math.exp(x ** 2)

def floatRange(start, end, increment):
    i = start
    while i < end:
        yield i
        i += increment

def simpsonsRule(a, b):
    n = 100000
    L = []
    i = 0
    h = (b - a)/n
    Sn = 0

    L = list(floatRange(a, b, h))
    L.append(b)
    
    while i <= n:
        if (i == 0) or (i == n):
            c = 1
        elif i % 2 == 0:
            c = 4
        else:
            c = 2
        Sn = c * myFunction(L[i]) + Sn
        i += 1
    
    Sn = Sn * (h/3)    
    
    return Sn

###### Begin Main ######

import math

a = int(input("Please enter the lower bound of integration: "))
b = int(input("Please enter the upper bound of integration: "))
ans = simpsonsRule(a, b)

print(ans)
