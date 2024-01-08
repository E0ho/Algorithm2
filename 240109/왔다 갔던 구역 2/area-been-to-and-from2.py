n = int(input())

x = 100

count_list = [
    0 for i in range(202)
]

for _ in range(n):
    count, dir = input().split()
    count = int(count)

    for _ in range(count):
        if dir == "R":
            x += 1
            count_list[x] += 1

        else:
            x -= 1
            count_list[x] += 1

cnt = 0
for ele in count_list:
    if ele >= 2:
        cnt += 1

print(cnt)