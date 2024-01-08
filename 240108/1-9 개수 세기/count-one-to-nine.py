n = int(input())
num = list(map(int, input().split()))

arr = [0 for i in range(1, 10)]

for ele in num:
    arr[ele - 1] = arr[ele - 1] + 1

for ele in arr:
    print(ele)