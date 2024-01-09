n = int(input())

# 격자 생성
grid = [
    list(input())
    for _ in range(n)
]

# 초기 값
dir_num = 0

def in_range(r, c):
    return 0 <= r and 0 <= c and r < n and c < n

# 북 동 남 서
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]

k = int(input())
t = 0
if k <= n:
    r = 0
    c = k -1
    dir_num = 2

elif k <= 2*n:
    r = k - n - 1
    c = n-1
    dir_num = 3

elif k <= 3*n:
    r = n-1
    c = n - k - 2*n
    dir_num = 0

else:
    r = n - k - 3*n
    c = 0
    dir_num = 1

while in_range(r, c):
    t += 1
    if grid[r][c] == "\\":
        dir_num = 3 - dir_num
        r = r + drs[dir_num]
        c = c + dcs[dir_num]
    else:
        if dir_num == 0:
            dir_num = 1

        elif dir_num == 1:
            dir_num = 0

        elif dir_num == 2:
            dir_num = 3

        else:
            dir_num = 2

        r = r + drs[dir_num]
        c = c + dcs[dir_num]
print(t)