def computeGCD(x, y):
    while(y):
        x, y = y, (x%y)
    return x

print(computeGCD(48, 64))
