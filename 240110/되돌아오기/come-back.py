# 입력
n = int(input())

# 초기 값
x, y = 0, 0
t = 0
dir_num = 0
arrive = False
# 방향 설정 (북 동 남 서)
dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]

dir_mapper = {
    "N":0,
    "E":1,
    "S":2,
    "W":3
}


# n번 이동
for _ in range(n):
    direction, num = input().split()
    num = int(num)
    dir_num = dir_mapper[direction]

    for _ in range(num):
        x = x + dxs[dir_num]
        y = y + dys[dir_num]

        t += 1
        if x == 0 and y == 0:
            print(t)
            arrive = True
            break
    
if arrive:
    pass
else:
    print(-1)