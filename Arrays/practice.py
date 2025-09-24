from array import *

# Create an array and traverse
my_array = array('i', [1, 2, 3, 4, 5])

print("Step 1")
for i in my_array:
    print(i)
    
# Access individual elements through indexes
print("Step 2")
print(my_array[0])

# Append any value in the array using append()
print("Step 3")
my_array.append(6)
print(my_array)

# Insert a value using the insert method
print("Step 4")
my_array.insert(3, 7)
print(my_array)

# Extend array using extend method
print("Step 5")
my_array1 = array('i', [10, 11, 12])
my_array.extend(my_array1)
print(my_array)

# remove element from using remove() method
print("Step 6")
my_array.remove(11)
print(my_array)

# remove last element using pop() method
print("Step 8")
my_array.pop()
print(my_array)

# 