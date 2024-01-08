n, m = tuple(map(int, input().split()))

grid = [
    [0] * m
    for _ in range(n)
]

cnt = 0
for j in range(m):
    
    for i in range(n):
        if j % 2 == 0:
            grid[i][j] = cnt
        else:
            grid[n-1-i][j] = cnt

        cnt += 1


for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
    print()