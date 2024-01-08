n = int(input())

binary = 1
sum_val = 0

while n > 0:

    r = n % 10      # 나머지
    n = n // 10     # 몫
    
    sum_val += r * binary
    # print(sum_val)
    binary *= 2

print(sum_val)