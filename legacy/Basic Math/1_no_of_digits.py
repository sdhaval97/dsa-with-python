# code to get the number of digits

user_input = int(input("Enter a number: "))

number_to_list = list(str(user_input))

counter = 0
for number in number_to_list:
    counter += 1
    
print(f"{user_input} has {counter} digits.")

# more efficient way using log10
import math

if user_input == 0:
    print(f"{user_input} has 1 digit.")
else:
    print(f"{user_input} has {math.floor(math.log10(abs(user_input)))+ 1} digits")
    