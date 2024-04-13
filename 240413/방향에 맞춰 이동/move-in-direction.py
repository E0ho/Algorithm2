# n번 이동하기
# 최종 위치 출력

# 입력
n = int(input())
direction_map = {
    'N':0,
    'E':1,
    'S':2,
    'W':3
}

# dx, dy 테크닉 (북,동,남,서)
dxs = [0,1,0,-1]
dys = [1,0,-1,0]

x, y = 0, 0
for _ in range(n):

    # 방향, 반복
    direction, num = input().split()
    num = int(num)

    dir_num = direction_map[direction]

    for _ in range(num):
        x = x + dxs[dir_num]
        y = y + dys[dir_num]

print(x, y)