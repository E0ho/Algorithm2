# 테두리
# i = 0, n-1
# j = 0, n-1

# r > c

n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1:
            print("*", end=" ")
        
        elif j == 0 or j == n-1:
            print("*", end=" ")
        
        elif i > j:
            print("*", end=" ")
        
        else:
            print(" ", end=" ")

    print()