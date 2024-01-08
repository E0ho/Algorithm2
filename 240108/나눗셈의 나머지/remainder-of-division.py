a, b = tuple(map(int, input().split()))

count_list = [0] * b

while a > 1:
    r = a % b
    count_list[r] += 1

    a = a // b
    
result = [i ** 2 for i in count_list]

sum_val = 0
for i in result:
    sum_val += i

print(sum_val)