# 입력
command = input()

# 초기 값
x, y = 0, 0
t = 0
dir_num = 0
result = 0

# 방향 (북, 동, 남, 서)
dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]

for c in command:
    t += 1
    if c == "L":
        dir_num = (dir_num -1 + 4) % 4
    elif c == "R":
        dir_num = (dir_num + 1) % 4
    else:
        x = x + dxs[dir_num]
        y = y + dys[dir_num]

        if x == 0 and y == 0:
            result = t
            print(t)
            break
    
    if result:
        break

if not result:
    print(-1)