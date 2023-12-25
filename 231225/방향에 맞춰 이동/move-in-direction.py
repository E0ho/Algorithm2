x, y = 0, 0

n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dir_map = {"E":0, "S":1, "W":2, "N":3}
     
for i in range(n):
    dir_num, repeat = input().split()
    repeat = int(repeat)

    dir_num = dir_map[dir_num]

    for i in range(repeat):
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)