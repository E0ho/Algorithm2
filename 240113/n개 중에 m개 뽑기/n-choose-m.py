n, m = tuple(map(int, input().split()))

# 각 자리의 수
arr = []
total = []

def choose(floor):

    # M개 조합 완성
    if floor == m+1:

        # 중복 검사
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[j] == arr[i]:
                    return
        
        # 출력
        # print(arr)
        total.append(list(arr))
        return
    
    # 가능한 모든 조합
    for i in range(1, n+1):
        arr.append(i)
        choose(floor+1)
        arr.pop()
a = []
choose(1)
# print(total)
for ele in total:
    ele.sort()
    a.append(ele)

length = len(a)
num = 1
for i in range(length):
    for j in range(i+1, length):
        if a[i] == a[j]:
            a.pop(i)
            a.append(num)
            num += 1
            
for i in range(length - num + 1):

    for ele in a[i]:
        print(ele, end=" ")
    print()