import math

def calculation(val):
    newval = val ** 21
    newval = math.log10(newval)
    newval = math.floor(newval)

    return newval


for i in range(1 ,10000):
    print(calculation(i))