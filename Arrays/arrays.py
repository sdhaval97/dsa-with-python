import array

my_array = array.array('i')
print(my_array)

my_array1 = array.array('i', [1, 2, 3, 4])
print(my_array1)


my_array1.insert(0, 6)
print(my_array1)

def traverseArray(array):
    for i in array:
        print(i)

traverseArray(my_array1)

def accessElement(array, index):
    if index > len(array):
        print("Index does not exist")
    else:
        print(array[index])
        
        