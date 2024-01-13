from collections import deque

n, k = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    list(0 for _ in range(n))
    for _ in range(n)
]

dq = deque()

# 북 동 남 서
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]
cnt = 0

def in_range(r, c):
    return 0 <= r and 0 <= c and r < n and c < n

def check(r, c):
    global cnt
    for dr, dc in zip(drs, dcs):
        nr = r + dr
        nc = c + dc

        if in_range(nr, nc) and grid[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                cnt += 1
                check(nr, nc)

for _ in range(k):
    r, c = map(int, input().split())
    check(r, c)
    
print(cnt)