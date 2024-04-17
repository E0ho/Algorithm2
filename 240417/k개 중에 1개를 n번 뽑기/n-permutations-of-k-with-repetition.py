# 1이상 k이하 숫자를 N번 고르기

# 입력
k, n = map(int, input().split())

li = []

def choose(idx):
    global answer
    if idx == n + 1:
        for comb in li:
            print(comb, end =" ")
        print()
        return
    
    for i in range(1, k+1):
        li.append(i)
        choose(idx + 1)
        li.pop()
    

choose(1)