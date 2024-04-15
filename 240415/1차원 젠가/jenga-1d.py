# n개의 층 젠가
# 1 ~ 100 이하 숫자
# 2번 특정 구간 빼기

# 입력
n = int(input())   # n층
li = []
for _ in range(n):
    li.append(int(input()))

# 제거 2번
for _ in range(2):
    s1, e1 = map(int, input().split())

    li = li[:s1 - 1] + li[e1:]

print(len(li))
for i in li:
    print(i)