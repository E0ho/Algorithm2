# 이동하며 숫자 채우기
# 격자 범위 나가기 직전 회전하기 (오른쪽, 아래, 왼쪽, 위)
# 이미 숫자가 채워져 있다면 회전

# 입력
n, m = map(int, input().split())

# 초기 값
r, c = 0, 0
num = 1
dir_num = 0
grid = [
    [0] * m
    for _ in range(n)
]

# dx, dy (오른쪽, 아래, 왼쪽, 위)
drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]

# 격자 범위 벗어남
def out_range(nr, nc):
    return (nr < 0 or nr >= n or nc < 0 or nc >= m)

# 격자 채우기
while True:

    # 모든 칸이 채워진 경우
    if num > (n * m):
        break

    # 채우고 + 1
    grid[r][c] = num
    num += 1

    # 예상 다음 칸
    nr = r + drs[dir_num]
    nc = c + dcs[dir_num]

    # 회전 조건
    if out_range(nr, nc):
        dir_num = (dir_num + 1) % 4
        nr = r + drs[dir_num]
        nc = c + dcs[dir_num]

    elif grid[nr][nc] != 0:
        dir_num = (dir_num + 1) % 4
        nr = r + drs[dir_num]
        nc = c + dcs[dir_num]
    
    # 이동
    r = nr
    c = nc

# 출력
for row in grid:
    for ele in row:
        print(ele, end = " ")
    print()