s = input()
result = ""
for c in s:
    if 'A' <= c and c <= 'Z':
        result += c.lower()
    else:
        result += c.upper()

print(result)