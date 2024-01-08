n = int(input())

o = ord('A')

for i in range(n):
    for j in range(i+1):

        if chr(o) == "Z":
            o = ord('A')

        print(chr(o), end="")
        o += 1

    print()