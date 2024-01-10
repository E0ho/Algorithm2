n, r, c = tuple(map(int, input().split()))

# n 번째 -> n Index
r -= 1
c -= 1

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 방향 (상, 하, 좌, 우)
drs = [-1, 1, 0, 0]
dcs = [0, 0, -1, 1]

# 범위 확인
def in_range(r, c):
    return 0 <= r and 0 <= c and r < n and c < n

# 초기값
num = grid[r][c]
dir_num = 0

while True:

    pre_num = num
    print(num, end=" ")

    # 상하좌우 확인
    for i in range(4):
        nr = r + drs[i]
        nc = c + dcs[i]

        if in_range(nr, nc) and grid[nr][nc] > num:
            r = r + drs[i]
            c = c + dcs[i]
            break

    num = grid[r][c]

    if num == pre_num:
        break