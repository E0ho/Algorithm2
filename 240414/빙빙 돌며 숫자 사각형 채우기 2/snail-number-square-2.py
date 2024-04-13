# n * m 크기 숫자 채우기

# 입력
n, m = map(int, input().split())

# 격자 초기화
grid = [
    [0] * m
    for _ in range(n)
]

# 초기 값
num = 1
r, c = 0, 0
dir_num = 0

# dx dy (남, 동, 북, 서)
drs = [1, 0, -1, 0]
dcs = [0, 1, 0, -1]

# 범위 검사 함수
def check_range(r, c):
    return r >= 0 and r < n and c >=0 and c < m

# 숫자 검사 함수
def check_num(r, c):
    return grid[r][c]

# 숫자 채우기
while num <= (n * m):

    grid[r][c] = num
    num += 1

    # 가상 이동
    nr = r + drs[dir_num]
    nc = c + dcs[dir_num]
    
    # 범위를 벗어남, 이미 숫자가 존재함
    if not check_range(nr, nc) or check_num(nr, nc):

        # 방향 전환
        dir_num = (dir_num + 1) % 4

        # 재이동
        nr = r + drs[dir_num]
        nc = c + dcs[dir_num]

    # 실제 이동
    r = nr
    c = nc
        
# 출력
for row in grid:
    for ele in row:
        print(ele, end = " ")
    print()