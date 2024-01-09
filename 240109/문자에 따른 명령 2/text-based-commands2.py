x, y = 0, 0

command = input()

dir_num = 0
# 북, 동, 남, 서
dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]

for c in command:
    if c == "L":
        dir_num = ((dir_num - 1) + 4) % 4

    elif c == "R":
        dir_num = (dir_num + 1) % 4

    else:
        x = x + dxs[dir_num]
        y = y + dys[dir_num]

print(x, y)