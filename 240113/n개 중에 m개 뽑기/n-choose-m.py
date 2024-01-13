n, m = tuple(map(int, input().split()))
arr = []

def choose(floor, num):
    # 출력 조건
    if floor == n+1:
        for ele in arr:
            print(ele, end=" ")
        print()

    # 1 ~ n이하 숫자 넣기
    for i in range(1, n+1):
        if i > num:
            arr.append(i)
            choose(floor+1, i)
            arr.pop()

        else:
            pass
    

choose(1, 0)