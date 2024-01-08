n = int(input())

# 1 ~ n+1
# i * j를 출력

for i in range(1, n+1):
    for j in range(n, 0, -1):
        print(i*j, end=" ")
    print()