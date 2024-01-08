n = int(input())

arr = list(map(int, input().split()))

result = [i ** 2 for i in arr]

for i in result:
    print(i, end=" ")