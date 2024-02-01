n = int(input())

# 초기 값
x = 0
y = 0

# 북 동 남 서
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

# 초기 방향
dir_num = 0

dir_map = {
    "N" : 0,
    "E" : 1,
    "S" : 2,
    "W" : 3
}

for _ in range(n):
    direction, count = input().split()
    count = int(count)

    dir_num = dir_map[direction]
    x += dxs[dir_num] * count 
    y += dys[dir_num] * count


print(x, y)