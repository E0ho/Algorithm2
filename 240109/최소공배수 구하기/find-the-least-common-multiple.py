n, m = tuple(map(int,input().split()))


cnt_n = 1
cnt_m = 1

first_n = n
first_m = m 

while n != m:
    if n > m:
        cnt_m += 1
        m = first_m * cnt_m


    elif n < m:
        cnt_n += 1
        n = first_n * cnt_n

print(n)