a = input()
b = input()

flag = True
cnt = 0
while a != b:
    cnt += 1
    a = a[-1] + a[:-1]

    if cnt > len(a):
        flag = False

if flag:
    print(-1)
else:
    print(cnt)