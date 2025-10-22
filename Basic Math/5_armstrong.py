def isArmstrong(x):
    original_number = x
    sum_digits = 0
    while x>0:
        last_digit = x % 10
        sum_digits += last_digit ** len(str(original_number))
        x //= 10
    return original_number == sum_digits

print(isArmstrong(153))

