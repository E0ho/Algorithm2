n = int(input())

n_list = list(map(int, input().split()))

max_n = 0
max_index = 0

while True:
    max_n = max(n_list)
    max_index = n_list.index(max_n)

    print(max_index + 1, end = " ")

    for i in range(max_index, n):
        n_list[i] = 0

    if max_index == 0:
        break