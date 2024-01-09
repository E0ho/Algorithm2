n = int(input())

li = list(input().split())

s = ""
for ele in li:
    s += ele

cnt = 0
for i in range(len(s)):
    print(s[i], end="")
    cnt += 1
    if cnt % 5 == 0:
        print()