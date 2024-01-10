n, t = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(2)
]

for _ in range(t):
    temp_1 = grid[0][n-1]
    temp_2 = grid[1][n-1]

    # 1행 이동
    for i in range(n-1, 0, -1):
        grid[0][i] = grid[0][i-1]
    grid[0][0] = temp_2


    # 2행 이동
    for i in range(n-1, 0, -1):
        grid[1][i] = grid[1][i-1]
    grid[1][0] = temp_1

for i in range(2):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()