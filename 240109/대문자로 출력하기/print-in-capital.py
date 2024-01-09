s = input()

upper_lower = ord('a') - ord('A')
result = ""

for c in s:
    if c.isalpha():
        if c < 'a':
            result += c
        else:
            temp = ord(c) - upper_lower
            result += chr(temp)

    else:
        pass

print(result)