n, t = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(2)
]

# 초기값
temp_1 = 0
temp_2 = 0

for _ in range(t):
    temp_1 = grid[0][n-1]
    temp_2 = grid[1][n-1]

    grid[0] = grid[0][:-1]
    grid[0].insert(0, temp_2)

    grid[1] = grid[1][:-1]
    grid[1].insert(0, temp_1)


for i in range(2):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()