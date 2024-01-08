# 2행 4열

li = [
    list(map(int, input().split()))
    for i in range(2)
]

sum_total = 0
for i in range(2):
    sum_col = 0
    for j in range(4):
        sum_col += li[i][j]
    print(f"{sum_col / 4 :.1f}", end=" ")
    sum_total += sum_col
print()

for i in range(4):
    sum_row = 0
    for j in range(2):
        sum_row += li[j][i]
    print(f"{sum_row / 2 :.1f}", end=" ")
print()

print(f"{sum_total / 8 :.1f}")