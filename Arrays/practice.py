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
my_array1 = array('i', [1, 10, 11, 12])
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

# fetching element using index()
print("Step 9")
print(my_array.index(5))

# reversing python array using the reverse() method
print("step 10")
my_array.reverse()
print(my_array)

# get array buffer info using buffer_info method
print("Step 11")
print(my_array.buffer_info())

# check for number of occurences using count()
print("Step 12")
print(my_array.count(1))

