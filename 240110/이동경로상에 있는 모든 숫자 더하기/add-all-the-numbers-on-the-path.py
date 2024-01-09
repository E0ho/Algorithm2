n, t = map(int, input().split())

s = input()

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 초기 값
r = n // 2
c = n // 2
dir_num = 0
sum_val = grid[r][c]

# 방향 (북, 동, 남, 서)
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]

def in_range(r, c):
    return 0 <= r and 0 <= c and r < n and c < n

for ch in s:
    if ch == "R":
        dir_num = (dir_num + 1) % 4
    elif ch == "L":
        dir_num = (dir_num + 3) % 4
    else:
        nr = r + drs[dir_num]
        nc = c + dcs[dir_num]

        if in_range(nr, nc):
            r = nr
            c = nc
            sum_val += grid[r][c]

        else:
            continue

print(sum_val)