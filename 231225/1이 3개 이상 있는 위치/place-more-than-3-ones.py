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

total = 0
for r in range(n):
    for c in range(n):

        cnt = 0
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc

            if in_range(nr, nc) and grid[nr][nc] == 1:
                cnt +=1

        if cnt >= 3:
            total += 1

print(total)