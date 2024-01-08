m = int(input())


# n 짝수 = /2
# n 홀수 = *3 +1

# n이 1이 될때 까지

for _ in range(m):
    cnt = 0
    n = int(input())

    while n != 1:
        cnt += 1

        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1

    print(cnt)