n, m = map(int, input().split())

grid = [
    [0] * m
    for _ in range(n)
]



# 범위
def in_range(r, c):
    return (0 <= r and 0 <= c and r < n and c < m)

# 동 남 서 북
drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]
dir_num = 0

num = 1
i = 0
j = 0
while num <= n * m:
    grid[i][j] = num
    num += 1
    temp_i = i + drs[dir_num]
    temp_j = j + dcs[dir_num]

    if in_range(temp_i, temp_j) and grid[temp_i][temp_j] == 0:
        i = temp_i
        j = temp_j

    else:
        dir_num = (dir_num + 1) % 4
        i = i + drs[dir_num]
        j = j + dcs[dir_num]


for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
    print()