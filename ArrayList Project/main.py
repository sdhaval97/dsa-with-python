# Calculate average temperature

numDays = int(input("How many day's temperature? "))
total_temp = 0
temp = []
for i in range(1, numDays+1):
    user_temp = int(input(f"Day {i} temperature: "))
    temp.append(user_temp)
    total_temp += user_temp
print(temp)
avg_temperature = total_temp / numDays
print(f"The average temperature is: {avg_temperature}")
daysAbove = 0
for i in range(len(temp)):
    if temp[i] > avg_temperature:
        daysAbove += 1
        print(f"Day {i+1} has temperature greater than the average temperature")

print(f"{daysAbove} day(s) have temperature greater than the average temperature")