n, m = tuple(map(int, input().split()))

grid = [
    [0] * n
    for _ in range(n)
]

for _ in range(m):
    x, y = tuple(map(int, input().split()))
    grid[x-1][y-1] = 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()