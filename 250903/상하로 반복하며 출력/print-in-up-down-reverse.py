N = int(input())


arr = [
    [0] * N
    for _ in range(N)
]

for i in range(N):
    if (i % 2 == 0):
        cnt = 1          
        for j in range(N):      
            arr[j][i] = cnt
            cnt += 1
    else :
        cnt = N
        for j in range(N):      
            arr[j][i] = cnt
            cnt -= 1

for line in arr:
    for ele in line:
        print(ele, end="")
    print()