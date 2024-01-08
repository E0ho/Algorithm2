n = int(input())

num = ord("A")
for i in range(n):
    for j in range(i):
        print(" ", end=" ")

    for i in range(n-i):
        print(chr(num), end=" ")
        num += 1

        if num > ord("Z"):
            num = ord("A") 
        
    print()