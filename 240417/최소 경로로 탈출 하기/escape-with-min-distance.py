# 최단거리

from collections import deque

# 입력
n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 재방문 방지
visited = [
    [0] * m
    for _ in range(n)
]

# 상하좌우
drs = [1, 0, -1, 0]
dcs = [0, 1, 0, -1]

# 격자 범위 내
def in_range(r, c):
    return 0<= r and 0 <= c and r < n and c < m

# 최단 경로 탐색
def bfs():
    global answer, count
    while q:
        r, c = q.popleft()

        if r == n-1 and c == m-1:
            answer = visited[r][c] - 1
        
        count = visited[r][c] + 1
        for dr, dc in zip(drs, dcs):
            nr = r + dr
            nc = c + dc

            # 격자 내 | 뱀 x | 방문 x
            if in_range(nr, nc) and grid[nr][nc] == 1 and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = count
            

answer = -1
q = deque()
q.append((0, 0))
visited[0][0] = 1
count = 0
bfs()

print(answer)