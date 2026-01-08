# brute force
def isPrime(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    
    if len(divisors) > 2:
        return False
    else:
        return True

# optimal solution
import math
def isPrimeOptimal(n):
    divisors = []
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            divisors.append(i)
            if (n/i != i):
                divisors.append(int(n/i))
    
    if len(divisors) > 2:
        return False
    return True
        

print(isPrimeOptimal(7))                
    
