n, t = tuple(map(int, input().split()))
r, c, d = input().split()

r = int(r) - 1
c = int(c) - 1

def in_range(nr, nc):
    return 0 <= nr and 0 <= nc and nr < n and nc < n

dir_map = {
    "U":0,
    "L":1,
    "R":2,
    "D":3
}

dir_num = dir_map[d]

# U, L, R, D (위, 좌, 오, 아래)
drs = [-1, 0, 0, 1]
dcs = [0, -1, 1, 0]

for _ in range(t):
    nr, nc = r + drs[dir_num], c + dcs[dir_num]

    if in_range(nr, nc):
        r, c = nr, nc
    else:
        dir_num = 3 - dir_num

print(r + 1, c + 1)