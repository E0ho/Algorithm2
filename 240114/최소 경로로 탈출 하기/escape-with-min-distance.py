from collections import deque
dq = deque()

n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    list(0 for _ in range(m))
    for _ in range(n)
]

# 남 동 북 서
drs = [1,0,-1,0]
dcs = [0,1,0,-1]

ans = -1


def in_range(r, c):
    return 0 <= r and 0 <= c and r < n and c < m

def bfs_move():
    global ans

    while dq:
        r, c, cnt = dq.popleft()
        cnt += 1
        
        if r == n - 1 and c == m - 1:
            ans = cnt
        
        for dr, dc in zip(drs, dcs):
            nr = r + dr
            nc = c + dc
            if in_range(nr, nc) and grid[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                dq.append((nr, nc, cnt))

visited[0][0] = 1
dq.append((0,0,-1))
bfs_move()

print(ans)