n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        if i % 2 != 0:
            if j % 2 != 0:
                print(1, end=" ")
            else:
                print(0, end=" ")
        elif i % 2 == 0:
            if j % 2 != 0:
                print(0, end=" ")
            else:
                print(1, end=" ")

    print()
    