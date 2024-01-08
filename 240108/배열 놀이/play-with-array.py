n, q = map(int, input().split())

n_list = list(map(int, input().split()))

for i in range(q):
    q_list = list(map(int, input().split()))

    if q_list[0] == 1:
        print(n_list[q_list[1] - 1])

    elif q_list[0] == 2:
        if q_list[1] in n_list:
            print(n_list.index(q_list[1]) + 1)

        else:
            print(0)
    
    else:
        for i in range(q_list[1] - 1, q_list[2]):
            print(n_list[i], end=" ")
        print()