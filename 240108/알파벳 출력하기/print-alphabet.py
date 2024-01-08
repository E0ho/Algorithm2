n = int(input())

c = "A"
o = ord(c)

for i in range(n):
    for j in range(i+1):
        print(chr(o), end="")
        o += 1

    print()