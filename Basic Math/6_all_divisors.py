def allDivisors(n):
    divisor_list = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor_list.append(i)
    
    return divisor_list

print(allDivisors(4))

            