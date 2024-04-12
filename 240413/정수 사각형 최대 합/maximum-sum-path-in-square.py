# 오른쪽 or 아래 // 이동 가능
# dx, dy 테크닉을 활용해, 좌측, 위의 값 중 더 큰 값을 더한다
# 0 패딩 주기 -> 첫번째 행, 열

# 입력
N = int(input())
li = [[0] * (N + 1)]       # 0 패딩
x, y = 1, 1

for _ in range(N):
    row = [0] + list(map(int, input().split()))
    li.append(row)

# 좌, 상 값 중 더 큰 값 더하기
for i in range(1, N + 1):
    for j in range(1, N + 1):
        big = max(li[i-1][j], li[i][j-1])
        li[i][j] += big

print(li[N][N])