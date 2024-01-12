k, n = map(int, input().split())

arr = []

# 박스의 갯수 = Floor
def choose(floor):
    if floor == n+1:
        for i in arr:
            print(i, end=" ")
        print()
        return

    # 가지 수 = 가능한 숫자
    for i in range(1, k+1):
        arr.append(i)
        choose(floor+1)
        arr.pop()

choose(1)