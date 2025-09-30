# Python Lists practice

# Accessing/Traversing
shoppingList = ['Milk', 'Cheese', 'Butter']
print(shoppingList[0])

# Traversing
for i in range(len(shoppingList)):
    print(shoppingList[i])

# Update/Insert list
# insert to insert anywhere
my_list = [1, 2, 3, 4, 5, 6]
my_list.insert(3, 10)
print(my_list)

# append to insert at the end (time efficient)
my_list.append(20)

# extend to add a new list
my_list.extend([10, 20, 30, 40, 5])
print(my_list)

def linear_search(list, target):
    for i, value in enumerate(list):
        if value == target:
            return i
    return -1

print(linear_search(my_list, 10))

# list comprehension
new_list = [3, 4, 5, 6, 7, 8]
double_list = [item * 2 for item in new_list]
print(double_list)
new_double_list = [item * 3 for item in new_list if item > 3]
print(new_double_list)
filtered_list = [item if item > 20 else 0 for item in new_double_list]
print(filtered_list)