n, m = tuple(map(int, input().split()))
# n개의 정점
# m개의 선

li = [[0] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

# 인접 리스트 채우기
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    li[x].append(y)
    li[y].append(x)


# 깊이 우선 탐색
def dfs(n):
    # [ [2,3], []]
    for ele in li[n]:
        if visited[ele] == 0:
            visited[ele] = 1
            dfs(ele)

# 방문 여부
visited[1] = 1
dfs(1)

ans = 0
for ele in visited:
    if ele == 1:
        ans += 1

print(ans - 2)