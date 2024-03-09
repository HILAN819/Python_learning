row = 8
for i in range(row + 1):
    for j in range(i):
        print(i, end="")
    print("")

n = int(input("Enter number: "))
for x in range(1, 20):
    G = n * x
    print(G)
