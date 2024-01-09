n = int(input())

li = [
    input()
    for _ in range(n)
]

sum_val = 0
for i in li:
    sum_val += int(i)

s = str(sum_val)
s = s[1:] + s[0]
print(s)