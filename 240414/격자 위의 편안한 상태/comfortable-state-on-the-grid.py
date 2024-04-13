# n * n 격자
# 총 m번 색칠
# 한번에 한칸 색칠
# 색칠한 직후 해당 칸 편안한 상태인지 확인
# 편안한 상태 : 위 아래 양옆 칸 중 색칠된 칸 3개인 경우

# 입력
n, m = map(int, input().split())

grid = [
    [0] * (n + 2)
    for _ in range(n + 2)
]

# 상화좌우 dx, dy 테그닉
drs = [0, 0, 1, -1]
dcs = [1, -1, 0 ,0]


# M번 색칠하기
for _ in range(m):
    r, c = map(int, input().split())

    # 해당 칸 색칠
    grid[r][c] = 1

    # 인접 칸 색칠 갯수
    temp_count = 0

    # 해당 칸 상하좌우 검사하기
    for dr, dc in zip(drs, dcs):
        nr = r + dr
        nc = c + dc

        if grid[nr][nc] == 1:
            temp_count += 1

    if temp_count == 3:
        print(1)
    else: print(0)