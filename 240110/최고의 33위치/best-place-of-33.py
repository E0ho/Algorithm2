n = int(input())

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

# 초기값
max_val = 0
temp = 0

# 탐색 함수
def count(i, j):
    value = 0
    for r in range(i, i+3):
        for c in range(i, i+3):
            if grid[r][c] == 1:
                value += 1

    return value

# 탐색
for i in range(n-2):
    for j in range(n-2):
        temp = count(i, j)
        max_val = max(temp, max_val)



# 출력
print(max_val)