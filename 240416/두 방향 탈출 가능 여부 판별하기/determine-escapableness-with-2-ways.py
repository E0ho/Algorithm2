# n * m 크기의 격자
# 뱀 피해서 n-1, m-1 까지 가기
# 아래, 오른쪽 2방향으로 이동
# 탈출 1 / 불가 0

# 입력
n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 인접칸 이동 dx, dy
drs = [1, 0]
dcs = [0, 1]

def in_range(r, c):
    return 0 <= r and 0 <= c and r < n and c < m
    
def dfs(r, c):

    # 도착 종료
    if r == n-1 and c == m-1:
        answer = 1
        return    

    # 뱀이 있는 경우
    if grid[r][c] == 0:
        return

    # 우측, 아래로 이동
    for dr, dc in zip(drs, dcs):
        nr = r + dr
        nc = c + dc
        if in_range(nr, nc):
            dfs(nr, nc)
    

answer = 0
dfs(0, 0)
print(answer)