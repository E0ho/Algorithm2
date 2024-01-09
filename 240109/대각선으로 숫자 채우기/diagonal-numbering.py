n, m = map(int,input().split())

grid = [
    [0] * m
    for _ in range(n)
]

cnt = 1
for i in range(n):
    for j in range(m):
        # 모든 배열 탐색 (0 이라면 cnt)
        if grid[i][j] == 0:
            grid[i][j] = cnt
            cnt += 1
        
        # 대각 이동
        s_row = i
        s_col = j

        # col이 0 보다 클때, row가 n-1보다 작을때
        while (s_col > 0) and (s_row < n - 1):
            s_col -= 1
            s_row += 1
            if grid[s_row][s_col] == 0:
                grid[s_row][s_col] = cnt
                cnt += 1

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
    print()