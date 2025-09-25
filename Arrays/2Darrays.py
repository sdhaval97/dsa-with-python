import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=0)
print(newTwoDArray)

newTwoDArray = np.append(twoDArray, [[1, 2, 3, 4]], axis=0)
print(newTwoDArray)

def accessElements(arr, rowindex, colindex):
    if rowindex >= len(arr) and colindex >= (arr[0]):
        print("IncorrWect index")
        
def TraverseArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j])
            
TraverseArray(newTwoDArray)

def search2DArray(arr, value):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == value:
                return value
    return 'The element is not found'
    