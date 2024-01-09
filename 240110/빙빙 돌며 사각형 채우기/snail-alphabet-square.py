n, m = map(int,input().split())

grid = [
    [0] * m
    for _ in range(n)
]

dir_num = 0
r, c = 0, 0
o = ord("A")

# 동 남 서 북
drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]


def in_range(r, c):
    return 0 <= r and 0 <= c and r < n and c < m

# 격자 채우기
for i in range(n*m):
    grid[r][c] = chr(o)
    o += 1
    
    if o > ord("Z"):
        o = ord("A")
        

    # 가상 이동
    nr = r + drs[dir_num]
    nc = c + dcs[dir_num]

    if not in_range(nr, nc) or grid[nr][nc] != 0:
        dir_num = (dir_num + 1) % 4
        nr = r + drs[dir_num]
        nc = c + dcs[dir_num]

    r = nr
    c = nc



# 출력
for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
    print()