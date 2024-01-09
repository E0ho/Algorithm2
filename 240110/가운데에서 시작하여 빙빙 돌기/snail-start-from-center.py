n = int(input())

# 격자 생성
grid = [
    [0] * n
    for _ in range(n)
]

# 초기 값
r = n // 2
c = n // 2
dir_num = 0
num = 1
count = 1

# 방향 (동, 북, 서, 남)
drs = [0, -1, 0, 1]
dcs = [1, 0, -1, 0]


def in_range(r, c):
    return 0 <= r and 0 <= c and r < n and c < n

# 북 -> 서
# 남 -> 동 
while num <= (n * n):
    
    for _ in range(count):
        grid[r][c] = num
        num += 1
        nr = r + drs[dir_num]
        nc = c + dcs[dir_num]

        if not in_range(nr, nc):
            break

        else:
            r = nr
            c = nc
    
    dir_num = (dir_num + 1) % 4
    nr = r + drs[dir_num]
    nc = c + dcs[dir_num]

    if dir_num == 0 or dir_num == 2:
        count += 1

   
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()