k, n = map(int, input().split())

arr = []



def choose(floor):
    if floor == n+1:
        for ele in arr:
            print(ele, end=" ")
        print()
        return

    for i in range(1, k+1):
        if floor != 1 and arr[-1] == i and arr[-2] == i:
            continue
        
        arr.append(i)
        choose(floor + 1)
        arr.pop()
    





choose(1)