n = int(input())

# 1 ~ 9 -> 1
# i == 0
# j >= i

cnt = 1
for i in range(n):
    for j in range(n):
        if j < i:
            print(" ", end=" ")

        else:
            print(cnt, end=" ")
            cnt += 1

            if cnt == 10:
                cnt = 1

    print()