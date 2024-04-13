# n * n 격자
# 상하좌우 이동 -> 1초에 1칸
# 1행 1열부터 시작 -> python에서는 0이니까 -1 진행
# 뒤집기 -> 1초

# 입력
n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r) - 1, int(c) - 1

mapping = {
    'U':3,       # 위
    'D':0,       # 아래 
    'R':1,       # 오른쪽
    'L':2        # 왼쪽
}

# dx, dy 테크닉 -> 인접 칸(남, 동, 서, 북) 이동
dcs = [0, 1, -1, 0]
drs = [1, 0, 0, -1] 

# 초기 방향
dir_num = mapping[d]

# 4초간 이동
for _ in range(t):

    r = r + drs[dir_num]
    c = c + dcs[dir_num]

    # 벽이라면 뒤집기
    if (r < 0 or r > n - 1 or c < 0 or c > n - 1):
        dir_num = 3 - dir_num 
        r = r + drs[dir_num]
        c = c + dcs[dir_num]

        
    
print(r + 1, c + 1)