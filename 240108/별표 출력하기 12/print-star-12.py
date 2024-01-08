n = int(input())

# r == 0 전체 출력

# c가 홀수 and c >= r 이면, 출력


for r in range(n):
    
    for j in range(n):

        # 0행 출력
        if r == 0:
            print("*", end=" ")

        # 0행 이상 -> c > r and c 홀수
        elif j % 2 != 0 and j >= r:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()