n = int(input())

# i = 0
# c >= r

for i in range(n):
    for j in range(n):
        if i == 0:
            print("*", end = " ")

        elif j >= i and j % 2 != 0:
            print("*", end = " ")
        
        else:
            print(" ", end = " ")

    print()