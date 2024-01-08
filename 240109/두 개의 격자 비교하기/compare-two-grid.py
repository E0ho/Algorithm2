n, m = tuple(map(int, input().split()))

first_grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

second_grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

result = [
    [0] * m
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        if first_grid[i][j] == second_grid[i][j]:
            result[i][j] = 0
        else:
            result[i][j] = 1

for i in range(n):
    for j in range(m):
        print(result[i][j], end=" ")
    print()