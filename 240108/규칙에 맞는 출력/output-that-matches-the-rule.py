n = int(input())

for i in range(n):
    cnt = n - i 
    for j in range(i+1):
        print(cnt, end=" ")
        cnt += 1

    print()