n = int(input("Enter the row size for the diamond: "))

for i in range(1, n+1):
    for k in range(n-i):
        print(" ", end=" ")
    for j in range(1, 2*i):
        print("*", end=" ")
    print()
for i in range(n-1, 0, -1):
    for k in range(n-i):
        print(" ", end=" ")
    for j in range(1,2*i ):
        print("*", end=" ")
    print()