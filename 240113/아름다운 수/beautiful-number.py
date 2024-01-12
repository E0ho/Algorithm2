# 1 ~ 4

n = int(input())
arr = []
ans = 0

def cnt():
    global ans

    index = 0
    while index < n:

        temp = arr[index]

        if temp > n - index:
            return

        for j in range(index, temp + index):
            if arr[index] != arr[j]:
                return

        index += temp

    ans += 1
    return


def choose(floor):

    if floor == n+1:
        cnt()
        return
    
    for i in range(1, 5):
        arr.append(i)
        choose(floor+1)
        arr.pop()


choose(1)
print(ans)