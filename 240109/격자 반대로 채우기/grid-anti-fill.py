n = int(input())

grid = [
    [0] * n
    for _ in range(n)
]

# 세로(행) 조건 필요
# 가로(열) 무조건 작아짐
cnt = 1
r_num = -1
for i in range(n-1, -1, -1):
    r_num += 1
    for j in range(n):

        if r_num % 2 == 0:
            grid[n - 1 - j][i] = cnt

        else:
            grid[j][i] = cnt

        cnt += 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end =" ")
    print()