n, m = map(int,input().split())

# 격자 생성
grid = [
    [0] * n
    for _ in range(n)
]

# 범위 함수
def in_range(r, c):
    return 0 <= r and 0 <= c and r < n and c < n

# 상하좌우 (북, 동, 남, 서)
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]

# 색칠 시작
for _ in range(m):
    r, c = map(int, input().split())

    r -= 1
    c -= 1

    cnt = 0

    # 색칠
    grid[r][c] = 1

    for i in range(4):
        nr = r + drs[i]
        nc = c + dcs[i]

        if in_range(nr, nc) and grid[nr][nc] == 1:
            cnt += 1
    
    if cnt == 3:
        print(1)

    else:
        print(0)