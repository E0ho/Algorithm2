# N * N 격자
# 1 ~ 100
# M개의 구슬이 1초에 상하좌우 인접한 곳 중 가장 큰 값으로 이동 
# 상하좌우 우선순위
# 충돌하면 사라짐
# t초 후 구슬의 수

def in_range(nr, nc, n):
    return 0 <= nr and 0 <= nc and nr < n and nc < n

# 입력
n, m, t = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 현재 공 위치 배열 초기화
current_ball = [
    [0] * n
    for _ in range(n)
]

# 공 위치 입력
for _ in range(m):
    r, c = map(int,input().split())
    current_ball[r-1][c-1] = 1


# 상하좌우 우선순위
drs = [-1, 1, 0, 0]
dcs = [0, 0, -1, 1]
temp_r = 0
temp_c = 0

for _ in range(t):

    # 다음 볼 위치 배열 초기화
    next_ball = [
        [0] * n
        for _ in range(n)
    ]

    # 모든 위치 탐색
    for i in range(n):
        for j in range(n):

            # 현재 위치 공이 있다면
            if current_ball[i][j] == 1:
                max_value = 0

                # 상하좌우 살피기
                for dr, dc in zip(drs, dcs):
                    nr = i + dr
                    nc = j + dc

                    # 최대값을 갖는 좌표 저장
                    if in_range(nr, nc, n):
                        if grid[nr][nc] > max_value:
                            max_value = grid[nr][nc]
                            temp_r = nr
                            temp_c = nc
                    
                # 상하좌우 중 가장 큰 값 좌표 다음 공 위치
                next_ball[temp_r][temp_c] += 1

    # 공 겹친 칸 제거
    for i in range(n):
        for j in range(n):
            if next_ball[i][j] > 1:
                next_ball[i][j] = 0
                
    # 모든 공 한번에 이동
    current_ball = []
    for row in next_ball:
        current_ball.append(row)

# 출력
count = 0
for i in range(n):
    for j in range(n):
        if current_ball[i][j] == 1:
            count += 1

print(count)