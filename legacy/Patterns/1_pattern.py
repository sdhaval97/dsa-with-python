# printing a square pattern
n = int(input("enter the number of rows"))
k = int(input("Enter the number of columns"))
for i in range(n):
    for j in range(k):
        print("*", end=" ")
    print()

    