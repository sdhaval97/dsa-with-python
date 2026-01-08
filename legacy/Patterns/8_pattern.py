n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    for k in range(n-i):
        print(" ", end=" ")
    for j in range(1, 2*i):
        print("*", end=" ")
    print()