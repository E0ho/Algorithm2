# 1 ~ 100이하의 숫자 ( n * n 격자 )
# 행복한 수열 : 연속해서 m개 이상의 동일한 원소가 나오는 순간
# 모든 행, 모든 열 중 행복한 수열의 개수 출력하기

# 입력
n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

count = 0
# 모든 행 검사
for i in range(n):
    row = []
    col = []
    for j in range(n):
        row.append(grid[i][j])
        col.append(grid[j][i])

    # 행 검사
    row_count = [1] * n
    for i in range(1, n):
        if row[i - 1] == row[i]:
            row_count[i] = row_count[i-1] + 1

    if max(row_count) >= m:
        count += 1

    # 열 검사
    col_count = [1] * n
    for i in range(1, n):
        if col[i - 1] == col[i]:
            col_count[i] = col_count[i-1] + 1
    
    if max(col_count) >= m:
        count += 1

print(count)