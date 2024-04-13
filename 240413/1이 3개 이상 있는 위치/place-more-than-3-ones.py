# N * N 격자
# 상하좌우 인전 칸 중 1이 적혀있는 수가 3개 이상인 곳의 개수
# 0 패딩

# 입력
n = int(input())

# 패딩을 두른 격자
grid = []
padding = [0] * (n + 2)
grid.append(padding)
for _ in range(n):
    grid.append([0] + list(map(int, input().split())) + [0])
grid.append(padding)

# dx, dy 테크닉 -> 상하좌우 인전 칸
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

total = 0


# 모든 칸 탐색
for i in range(1, n + 1):
    for j in range(1, n + 1):
        
        temp_count = 0

        # 상하좌우 탐색
        for dir_num in range(4):
            nx = i + dxs[dir_num]
            ny = j + dys[dir_num]

            if grid[nx][ny] == 1:
                temp_count += 1

        if temp_count >= 3:
            total += 1

print(total)