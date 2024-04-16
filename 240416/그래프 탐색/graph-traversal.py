# N개의 정점
# M개의 간선
# 1번 정점 시작


# 입력
n, m = map(int, input().split())


# 그래프
dic = {}
visited = {}        # 방문 여부
for _ in range(m):
    x, y = map(int, input().split())
    
    # 연결 그래프 표현
    dic[x] = dic.get(x, [])
    dic[y] = dic.get(y, [])
    visited[x] = 0
    visited[y] = 0
    dic[x].append(y)
    dic[y].append(x)


def dfs(n):
    for vertex in dic[n]:
        # 방문한적이 없다.
        if visited[vertex] == 0:
            visited[vertex] = 1
            dfs(vertex)

# 탐색
dfs(1)
visited[1] = 0

print(sum(visited.values()))