n = int(input())

# i와 n-1-i 반복

for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            print(i + 1, end="")
        else:
            print(n - i, end="")
            
    print()