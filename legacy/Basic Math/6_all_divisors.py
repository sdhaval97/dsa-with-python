def allDivisors(n):
    divisor_list = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor_list.append(i)
    
    return divisor_list

print(allDivisors(4))

# optimal solution
import math
def isPrimeOptimal(n):
    divisors = []
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            divisors.append(i)
            if (n/i != i):
                divisors.append(int(n/i))
    
    return divisors

print(isPrimeOptimal(36))   