n = int(input())

def in_range(nr, nc):
    return 0 <= nr and 0 <= nc and nr < n and nc < n

grid = []
for i in range(n):
    arr = list(map(int, input().split()))
    grid.append(arr)

# 북 동 남 서
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]

cnt = 0
for r in range(n):
    for c in range(n):

        near_cnt = 0
        for i in range(4):
            nr, nc = r + drs[i], c + dcs[i]
            if in_range(nr, nc) and grid[nr][nc] == 1:
                near_cnt +=1

        if near_cnt >= 3:
            cnt += 1

print(cnt)