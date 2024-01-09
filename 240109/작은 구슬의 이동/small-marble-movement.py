# 입력
n, t = map(int, input().split())
r, c, d = input().split()
r = int(r) - 1
c = int(c) - 1

# 격자 생성
grid = [
    [0] * n
    for _ in range(n)
]

# d = U, L, R, D 방향
drs = [-1, 0, 0, 1]
dcs = [0, -1, 1, 0]
dir_num = 0

if d == "U":
    dir_num = 0
elif d == "L":
    dir_num = 1
elif d == "R":
    dir_num = 2
else:
    dir_num = 3


# 격자 범위
def in_range(r, c):
    return (0 <= r and 0 <= c and r < n and c < n)


for _ in range(t):
    nr = r + drs[dir_num]
    nc = c + dcs[dir_num]

    if in_range(nr, nc):
        r = nr
        c = nc
    else:
        dir_num = 3 - dir_num

print(r + 1, c + 1)