def is_palindrome(n):
    if n < 0:
        return False
    original = n
    reverse = 0
    while n > 0:
        last_digit = n%10
        reverse = reverse * 10 + last_digit
        n //= 10
    return original == reverse

        
print(is_palindrome(121))
    