n = int(input())

li = [
    [0] * n
    for _ in range(n)
]

cnt = 1
for i in range(n):
    for j in range(n):
        li[j][i] = cnt 
        cnt += 1      

for i in range(n):
    for j in range(n):
        print(li[i][j], end = " ")
    print()