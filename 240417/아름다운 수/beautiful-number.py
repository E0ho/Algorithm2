# 1 ~ 4 이하 숫자들
# 해당 숫자만큼 연달아 나오는 숫자 = 아름다운 수

from collections import deque

# 입력 
n = int(input())

li = []
count = 0

def check(li):
    q = deque(li)

    while q:
        target = q[0]

        for _ in range(target):
            if not q:
                return 0
                
            c = q.popleft()
            if c != target:
                return 0
    
    return 1

# n자리 수
def choose(num):
    global count
    # n 자리 수 종료
    if num == n + 1:
        count += check(li)
        return

    for i in range(1, 5):
        li.append(i)
        choose(num + 1)
        li.pop()

choose(1)
print(count)