n = int(input())

n_list = list(map(int, input().split()))



for i in range(n):
    for j in range(i, n):
        ele = n_list[i]
        if ele < n_list[j]:
            n_list[i], n_list[j] = n_list[j], n_list[i]

    
for i in range(2):
    print(n_list[i], end=" ")