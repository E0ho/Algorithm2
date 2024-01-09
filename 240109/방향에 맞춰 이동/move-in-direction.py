n = int(input())

x, y = 0, 0

# 동 서 남 북
dxs = [1, -1, 0, 0]
dys = [0, 0, -1, 1]

dir_num = 0
for _ in range(n):
    direction, count = input().split()
    count = int(count)

    if direction == "E":
        dir_num = 0
    elif direction == "W":
        dir_num = 1
    elif direction == "S":
        dir_num = 2
    else:
        dir_num = 3

    x = x + dxs[dir_num] * count
    y = y + dys[dir_num] * count

print(x, y)