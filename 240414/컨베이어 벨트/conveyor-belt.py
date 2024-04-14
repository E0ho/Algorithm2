# 입력
n, t = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

# 결합
li = first + second

for _ in range(t):
    
    temp = li[2 * n - 1]

    for i in range(2 * n - 2, -1, -1):
        li[i + 1] = li[i]
    
    li[0] = temp

for i in range(2*n):
    if i == n:
        print()
    
    print(li[i], end= " ")