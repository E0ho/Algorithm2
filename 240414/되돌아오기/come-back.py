# (0, 0)에서 시작 -> 돌아오는 시간 구하기
# N 번 -> 방향, 거리 입력
# 1초에 1칸

# 입력
n = int(input())

# 초기 값
r, c = 0, 0

# dx, dy (북 동 남 서)
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]
mapping = {
    'N':0,
    'E':1,
    'S':2,
    'W':3
}
flag = False
time = 0
for _ in range(n):
    dir_s, count = input().split()
    count = int(count)

    dir_num = mapping[dir_s]

    # 이동
    for i in range(count):
        r = r + drs[dir_num]
        c = c + dcs[dir_num]

        time += 1
        if r == 0 and c == 0:
            print(time)
            flag = True
            break

    if flag:
        break