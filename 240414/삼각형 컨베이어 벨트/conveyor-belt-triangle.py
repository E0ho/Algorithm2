# 입력
n, t = map(int, input().split())

li = []
li = li + list(map(int, input().split()))
li = li + list(map(int, input().split()))
li = li + list(map(int, input().split()))


for _ in range(t):
    
    # 가장 마지막 값 저장
    temp = li[len(li) - 1]

    for i in range(3 * n - 1, 0, -1):
        li[i] = li[i - 1]
    
    li[0] = temp

# 출력
for i in range(3 * n):
    if i % n == 0 and i != 0:
        print()
    print(li[i], end=" ")