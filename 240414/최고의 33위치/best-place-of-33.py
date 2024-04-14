# N * N 격자
# 동전 = 1
# 3 * 3 사각형 내 동전 개수 최대로 하는 프로그램

# 입력
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

answer = 0
for i in range(n - 2):
    for j in range(n - 2):

        # 현재 위치를 시작점으로하는 사각형 내 동전 개수
        count = 0
        for a in range(3):
            for b in range(3):
                if grid[i + a][j + b] == 1:
                    count += 1
        
        # 최대값 갱신
        if answer < count:
            answer = count

print(answer)