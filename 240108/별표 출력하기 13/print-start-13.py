n = int(input())

for i in range(2*n):
    if i % 2 == 0 :
        for _ in range(n - i//2):
            print("*", end=" ")
        print()

    else:
        for _ in range(i // 2 + 1):
            print("*", end=" ")
        print()