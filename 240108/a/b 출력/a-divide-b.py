a, b = map(int, input().split())

s = ""
for i in range(21):
    mock = a // b
    s += str(mock)

    if i == 0:
        s += '.'

    a = a % b
    a *= 10
    

print(s)

# 3 / 5 -> 0          -> 3
# 30 / 5 -> 6         -> 0