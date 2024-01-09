s, q = input().split()
q = int(q)

for _ in range(q):
    question, a, b = input().split()

    if question == '1':
        a, b = int(a), int(b)
        s = list(s)
        s[a-1], s[b-1] = s[b-1], s[a-1]
        for ele in s:
            print(ele, end="")
        print()

    elif question == '2':
        s = "".join(s)
        s = s.replace(a, b)
        print(s)

    else:
        pass