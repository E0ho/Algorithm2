a = input()
b = input()

while b in a:
    index = a.find(b)
    a = a[:index] + a[index + len(b):]

print(a)