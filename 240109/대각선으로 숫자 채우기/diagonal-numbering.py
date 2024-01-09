n, m = map(int, input().split())

grid = [
    [0] * m
    for _ in range(n)
]

def in_range(r, c):
    return (0 <= r and 0 <= c and r < n and c < m)

dr = 1
dc = -1
cnt = 1

for i in range(n):
    for j in range(m):
        temp_i = i
        temp_j = j
        while in_range(temp_i, temp_j) and grid[temp_i][temp_j] == 0:
            grid[temp_i][temp_j] = cnt
            cnt += 1
            temp_i = temp_i + dr
            temp_j = temp_j + dc

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
    print()