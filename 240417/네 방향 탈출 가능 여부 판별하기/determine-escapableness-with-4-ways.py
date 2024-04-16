# n * m
# (0, 0) -> (n-1, m-1) 이동

from collections import deque

# 입력
n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 상화좌우 이동 중 재방문 방지
visited = [
    [0] * m
    for _ in range(n)
]

# 상하좌우 인접칸 이동
drs = [1, 0, 0, -1]
dcs = [0, 1, -1, 0]

# 범위 내
def in_range(nr, nc):
    return 0 <= nr and 0 <= nc and nr < n and nc < m

# 넓이 우선 탐색
def bfs():
    global answer

    while q:
        r, c = q.popleft()
        
        # 도착 시 종료
        if r == n-1 and c == m-1:
            answer = 1
            return
        
        # 상하좌우 이동
        for dr, dc in zip(drs, dcs):
            nr = r + dr
            nc = c + dc

            # 격자 내 | 방문 x | 뱀 x
            if in_range(nr, nc) and visited[nr][nc] == 0 and grid[nr][nc] != 0:
                q.append((nr, nc))
                visited[nr][nc] = 1

q = deque()
answer = 0
q.append((0,0))
visited[0][0] = 1
bfs()

print(answer)