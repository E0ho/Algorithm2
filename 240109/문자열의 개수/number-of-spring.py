li = []
while True:
    s = input()

    if s == '0':
        break

    li.append(s)

print(len(li))
for i in range(len(li)):
    if i % 2 == 0:
        print(li[i])