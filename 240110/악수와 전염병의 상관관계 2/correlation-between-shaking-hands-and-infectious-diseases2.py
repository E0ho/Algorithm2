N, K, P, T = tuple(map(int, input().split()))

time_line = []

people = [
    0 for i in range(N)
]

people[P-1] = 1

# 입력
for _ in range(T):
    t_x_y = list(map(int, input().split()))
    time_line.append(t_x_y)

# time_line 정렬
time_line.sort()

for ele in time_line:
    x = ele[1] - 1
    y = ele[2] - 1

    if (people[x] >= 1 and people[x] <= K) or (people[y] >= 1 and people[y] <= K):
        people[x] += 1
        people[y] += 1

for ele in people:
    if ele > 0:
        print(1, end="")
    else:
        print(0, end="")