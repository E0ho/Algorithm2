n, m = tuple(map(int, input().split()))
arr = []
visited = [ 0 for _ in range(n+1) ]


def choose(floor, num):
    if floor == m+1:
        for ele in arr:
            print(ele, end=" ")
        print()
        return

    for i in range(1, n+1):
        if i > num and visited[i] == 0:
            arr.append(i)
            visited[i] = 1
            choose(floor + 1 , i)
            arr.pop()
            visited[i] = 0


choose(1, 0)
# def choose(floor, num):
#     # 출력 조건
#     if floor == m + 1:
#         for ele in arr:
#             print(ele, end=" ")
#         print()
#         return

#     # 1 ~ n이하 숫자 넣기
#     for i in range(1, n + 1):
#         if i > num:
#             arr.append(i)
#             choose(floor + 1, i)
#             arr.pop()

#         else:
#             pass
    
# choose(1, 0)