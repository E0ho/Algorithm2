a = input()
b = input()

flag = False
cnt = 0
while a != b:
    cnt += 1
    a = a[-1] + a[:-1]

    if cnt > len(a):
        flag = True
        break

if flag:
    print(-1)
else:
    print(cnt)