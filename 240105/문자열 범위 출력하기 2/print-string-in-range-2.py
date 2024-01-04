s = input()
n = int(input())

if n > len(s):
    print(s[::-1])

else:
    for i in range(-1, -1-n, -1):
        print(s[i], end="")