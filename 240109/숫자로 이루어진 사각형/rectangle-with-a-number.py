n = int(input())

def grid_cnt(n):
    cnt = 1
    for i in range(n):
        for j in range(n):
            print(cnt, end=" ")
            cnt += 1
            if cnt == 10:
                cnt = 1
        print()

grid_cnt(n)