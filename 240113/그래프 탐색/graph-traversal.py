n, m = tuple(map(int, input().split()))

grid = [
    list(0 for _ in range(n+1))
    for _ in range(n+1)
    ]

visited = [0 for _ in range(n+1)]
ans = 0

for _ in range(m):
    x, y = tuple(map(int, input().split()))
    grid[x][y] = 1
    grid[y][x] = 1


def dfs(vertex):
    global ans
    for i in range(1, n+1):
        if grid[vertex][i] != 0 and visited[i] == 0:
            visited[i] = 1
            dfs(i)
            ans += 1



visited[1] = 1
dfs(1)
print(ans)




# # 인접 리스트 채우기
# for _ in range(m):
#     x, y = tuple(map(int, input().split()))
#     li[x].append(y)
#     li[y].append(x)

# ans = 0

# # 깊이 우선 탐색
# def dfs(n):
#     global ans
#     for ele in li[n]:
#         if visited[ele] == 0:
#             visited[ele] = 1
#             ans += 1
#             dfs(ele)

# # 방문 여부
# visited[1] = 1
# dfs(1)

# print(ans - 1)