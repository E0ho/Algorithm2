n = int(input())

# 2, 4, 6, 8 -> 2, 4

k = 2
for i in range(n):
    for j in range(n):
        print(k, end=" ")
        k += 2
        if k == 10:
            k = 2

    print()