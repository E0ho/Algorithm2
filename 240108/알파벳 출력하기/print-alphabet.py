n = int(input())

o = ord('A')

for i in range(n):
    for j in range(i+1):

        print(chr(o), end="")

        if chr(o) == "Z":
            o = ord('A') - 1
        
        o += 1

    print()