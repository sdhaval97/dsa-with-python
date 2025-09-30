# find the missing number in an array

def missing_number(my_list, total_count):
    sum_of_n = total_count * (total_count + 1)/2
    sum_of_array = sum(my_list)
    return sum_of_n - sum_of_array
print(missing_number([1, 2, 3, 4, 6], 6))