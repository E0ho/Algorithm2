n = int(input())

# grid 생성
grid = [
    [0] * n
    for _ in range(n)
]

# 파스칼 삼각형 채우기
for i in range(n):
    for j in range(i + 1):
        if j == 0:
            grid[i][j] = 1
        else:
            grid[i][j] = grid[i-1][j-1] + grid[i-1][j] 


# 출력
for i in range(n):
    for j in range(n):
        if grid[i][j] != 0:
            print(grid[i][j], end=" ")    
    print()