grid = [
    [0] * 5
    for _ in range(5)
]

for i in range(5):
    for j in range(5):
        if i == 0 or j == 0:
            grid[i][j] = 1
        
        else:
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
for i in range(5):
    for j in range(5):
        print(grid[i][j], end=" ")
    print()