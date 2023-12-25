x, y = 0, 0
dir_num = 0

s = input()

# 북 동 남 서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for c in s:
    if c == "L":
        dir_num -= 1
    elif c == "R":
        dir_num += 1
    elif c == "F":
        x, y = x + dx[(dir_num + 4) % 4], y + dy[(dir_num + 4) % 4]
    else:
        print("잘못된 입력")

print(x, y)