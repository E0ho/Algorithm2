n = int(input())

# 격자 생성
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

ans = 0
# 북 동 남 서
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]


# 격자 범위 검사 함수
def in_range(r, c):
    return 0 <= r and 0 <= c and r < n and c < n


# 상하좌우 인접 칸 검사 함수
def check(r, c):
    count = 0

    # 상화좌우 검사
    for i in range(4):
        nr = r + drs[i]
        nc = c + dcs[i]

        # 격자 범위 내 칸이며 1을 갖는 칸 count
        if in_range(nr, nc) and grid[nr][nc] == 1:
            count += 1

        if count == 3:
            return 1

    return 0

# 격자 내 모든 칸 검사 반복
for r in range(n):
    for c in range(n):
        ans += check(r, c)
        
print(ans)