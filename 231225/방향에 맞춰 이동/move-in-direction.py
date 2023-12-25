x, y = 0, 0

n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

     
for i in range(n):
    dir_num, repeat = input().split()
    repeat = int(repeat)

    if dir_num == "E":
        dir_num = 0
    elif dir_num == "S":
        dir_num = 1
    elif dir_num == "W":
        dir_num = 2
    else:
        dir_num = 3

    for i in range(repeat):
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)