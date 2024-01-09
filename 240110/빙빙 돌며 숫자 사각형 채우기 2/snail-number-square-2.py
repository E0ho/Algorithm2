n, m = map(int, input().split())

# 빈 Grid 생성
grid = [
    [0] * m
    for _ in range(n)
]

# 초기값
num = 1
r, c = 0, 0
dir_num = 0


# 남 동 북 서
drs = [1, 0, -1, 0]
dcs = [0, 1, 0, -1]

# 격자 범위 확인
def in_range(r, c):
    return 0 <= r and 0 <= c and r < n and c < m

# 모든 숫자 넣기
while num <= n * m:
    grid[r][c] = num
    num += 1
    nr = r + drs[dir_num]
    nc = c + dcs[dir_num]

    # 범위 이탈 or 이미 방문 
    if not in_range(nr, nc) or grid[nr][nc] != 0:
        dir_num = (dir_num + 1) % 4
        nr = r + drs[dir_num]
        nc = c + dcs[dir_num]

    r = nr
    c = nc


for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
    print()