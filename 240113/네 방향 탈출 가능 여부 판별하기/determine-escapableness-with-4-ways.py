n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    list(0 for _ in range(m))
    for _ in range(n)
]

# 초기값
ans = 0

# 북 동 남
drs = [-1, 0, 1]
dcs = [0, 1, 0]

def in_range(r,c):
    return (0 <= r and 0 <= c and r < n and c < m)


# 상하좌우 살펴보기 & 뱀 여부 확인 (이동)
def move(r, c):
    global ans
    if r == n - 1 and c == m - 1:
        ans = 1
        return
    
    for i in range(3):
        nr = r + drs[i]
        nc = c + dcs[i]

        if in_range(nr, nc) and grid[nr][nc] != 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                move(nr, nc)

visited[0][0] = 1
move(0, 0)
print(ans)













# n, m = tuple(map(int, input().split()))

# grid=[
#     list(map(int, input().split()))
#     for _ in range(n)
# ]

# visited = [
#     list(0 for i in range(m))
#     for _ in range(n)
# ]

# # 남 동
# drs = [1, 0]
# dcs = [0, 1]

# # 초기값
# r = 0
# c = 0
# ans = 0

# # 격자 내 위치
# def in_range(r, c):
#     return (0 <= r and 0 <= c and r < n and c < m)

# # 경로 탐색 시작
# def dfs(r, c):
#     global ans

#     if r == n-1 and c == m-1:
#         ans = 1
#         return
    
#     for dr, dc in zip(drs, dcs):
#         nr = r + dr
#         nc = c + dc

#         # 격자 탈출 시 1
#         if in_range(nr, nc) and grid[nr][nc] != 0:
#             if visited[nr][nc] == 0:
#                 visited[nr][nc] = 1
#                 dfs(nr, nc)

# visited[0][0] = 1
# dfs(0, 0)
# print(ans)