# (0, 0)에서 북쪽을 바라보고 시작
# N개의 명령에 따라 총 N번 이동
# L -> -90
# R -> +90
# F -> 이동

# 입력
cmd = input()

# dx, dy 테크닉 (북, 동, 남 ,서)
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

# 초기 값
x, y = 0, 0
dir_num = 0

for ele in cmd:

    # 전진
    if ele == 'F':
        x += dxs[dir_num]
        y += dys[dir_num]

    # -90 회전
    elif ele == 'L':
        dir_num = (dir_num + 3) % 4
    
    # +90 회전
    else:
        dir_num = (dir_num + 5) % 4

print(x, y)