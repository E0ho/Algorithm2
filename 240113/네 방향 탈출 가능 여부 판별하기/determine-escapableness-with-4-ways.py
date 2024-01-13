from collections import deque

n, m = tuple(map(int, input().split()))

# 행열 생성
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    list(0 for _ in range(m))
    for _ in range(n)
]

# queue
dq = deque()

# 남 동 북 서 (범위, 뱀)
drs = [1, 0, -1, 0]
dcs = [0, 1, 0, -1]

def in_range(r, c):
    return 0 <= r and 0 <= c and r < n and c < m



# 이동 (DFS - 재귀 , BFS - queue사용)
def move():
    global ans
    while dq:
        a, b = dq.popleft()

        if a == n - 1 and b == m - 1:
            ans = 1
            return

        for dr, dc in zip(drs, dcs):
            nr = dr + a
            nc = dc + b
            if in_range(nr, nc) and visited[nr][nc] == 0:
                if grid[nr][nc] != 0:
                    visited[nr][nc] = 1
                    dq.append((nr, nc))

ans = 0
dq.append((0,0))
move()
print(ans)