n, m = tuple(map(int, input().split()))

mi = min(n,m)

ma = 1
for i in range(1, mi):
    if n % i == 0 and m % i == 0:
        ma = i

print(ma)