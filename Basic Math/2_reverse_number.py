# reversing a number
n = int(input("Enter a number you want to reverse: "))
rev_num = 0
sign = -1 if n < 0 else 1
n = abs(n)
while n > 0:
    last_digit = n%10
    rev_num = rev_num * 10 + last_digit
    n //= 10
rev_num *= sign

# Check for 32-bit signed integer overflow
if rev_num < -2**31 or rev_num > 2**31 - 1:
    rev_num = 0

print(f"The reversed number is {rev_num}")

    