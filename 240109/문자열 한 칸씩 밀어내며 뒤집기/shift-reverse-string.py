s, q = input().split()
q = int(q)

for _ in range(q):
    command = int(input())

    if command == 1:
        s = s[1:] + s[0]
        
    elif command == 2:
        s = s[-1] + s[:-1]

    else:
        s = s[::-1]

    print(s)