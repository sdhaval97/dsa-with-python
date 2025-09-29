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
