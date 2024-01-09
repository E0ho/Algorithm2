n = int(input())

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return (0 <= x and 0 <= y and x < n and y < n)

# 북 동 남 서
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]

cnt = 0

for i in range(n):
    for j in range(n):

        temp_cnt = 0
        for k in range(4):
            nr = i + drs[k]
            nc = j + dcs[k]

            if in_range(nr, nc):
                if grid[nr][nc] == 1:
                    temp_cnt += 1

        if temp_cnt >= 3:
            cnt += 1

print(cnt)