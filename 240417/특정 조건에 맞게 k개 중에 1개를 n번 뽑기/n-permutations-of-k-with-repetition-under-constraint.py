# 1 ~ k 숫자 n번 고르기
# 연속해서 같은 숫자 3번 이상 제외

from itertools import product

# 입력
k, n = map(int, input().split())

li = []
for i in range(1, k+1):
    li.append(i)

combi = list(product(li, repeat = n))

for comb in combi:
    for i in range(len(comb)):
        print(comb[i], end= " ")
    print()