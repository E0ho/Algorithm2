first_rec = list(map(int, input().split()))
second_rec = list(map(int, input().split()))
offset = 1000

grid = [
    [0] * 2001
    for _ in range(2001)
]

for i in range(first_rec[1], first_rec[3] + 1):
    for j in range(first_rec[0], first_rec[2] + 1):
        grid[offset + i][offset + j] = 1

for i in range(second_rec[1], second_rec[3] + 1):
    for j in range(second_rec[0], second_rec[2] + 1):
        grid[offset + i][offset + j] = 0


min_r = 2000
min_c = 2000
max_r = 0
max_c = 0
for i in range(0, 2000):
    for j in range(0, 2000):
        if grid[i][j] == 1:
            if i > max_r:
                max_r = i

            if i < min_r:
                min_r = i

            if j > max_c:
                max_c = j
            
            if j < min_c:
                min_c = j

width = max_r - min_r
height = max_c - min_c

print(width * height)