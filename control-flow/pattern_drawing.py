size = int(input("Enter the size of the pattern: "))
rownum = 0

while rownum < size:
    for colnum in range(0, size):
        print("*", end="")
    print("\n")
    rownum += 1
