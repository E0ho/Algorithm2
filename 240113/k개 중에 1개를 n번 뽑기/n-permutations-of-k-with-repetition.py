k, n = map(int, input().split())

arr = []


def choose(floor):
    if floor == n+1:
        for i in arr:
            print(i, end=" ")
        print()
        return

    for i in range(1, k+1):
        arr.append(i)
        choose(floor+1)
        arr.pop()

choose(1)