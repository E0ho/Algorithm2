n = int(input())

n_list = list(map(int,input().split()))

max_val = 0
for i in range(n):
    for j in range(i, n):
        if max_val < n_list[j] - n_list[i]:
            max_val = n_list[j] - n_list[i]

print(max_val)