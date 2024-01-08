# n 합성수인지 판별
# 1보다 큰 자연수 중 소수가 아닌 수

n = int(input())

cnt = 0
for i in range(2, n):
    if n % i == 0:
        print("C")
        cnt += 1
        break

if cnt == 0 :
    print("N")