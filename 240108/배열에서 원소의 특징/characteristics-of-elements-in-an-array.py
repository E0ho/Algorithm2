arr = list(map(int, input().split()))

for ele in arr:
    if ele % 3 == 0:
        index = arr.index(ele)
        print(arr[index - 1])
        break