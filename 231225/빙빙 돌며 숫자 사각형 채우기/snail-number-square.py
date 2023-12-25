n, m = map(int, input().split())

grid = []
for i in range(n):
    grid.append([0] * m)

def in_range(i, j):
    return 0 <= i and 0 <= j and i < n and j < m

# 북, 동, 남, 서
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]

dir_num = 1
r, c = 0, 0
num = 2
grid[0][0] = 1


for _ in range(n * m - 1):
    
    nr, nc = r + drs[dir_num], c + dcs[dir_num]

    # 조건 x
    if not in_range(nr, nc) or grid[nr][nc] != 0:
        dir_num = (dir_num + 1) % 4
        nr, nc = r + drs[dir_num], c + dcs[dir_num]

    # 전진
    r, c = nr, nc

    # 숫자 대입
    grid[r][c] = num
    num += 1

    
    
for i in range(n):
    
    for j in range(m):
        print(grid[i][j], end = " ")
    print()