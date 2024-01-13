n = int(input())
arr = []
# 이미 추가한 수 확인 배열
visited = [
    0 for _ in range(n+1)
]

def choose(floor):
    # 종료 조건 (N칸이 넘어가면 현재까지 배열 출력)
    if floor == n+1:
        for ele in arr:
            print(ele, end=" ")
        print()

    for i in range(1, n+1):

        # 출력한 적 없는 수
        if visited[i] == 0:
            
            arr.append(i)
            visited[i] = 1
            choose(floor+1)
            arr.pop()
            visited[i] = 0

choose(1)