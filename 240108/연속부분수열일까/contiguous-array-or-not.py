n1, n2 = tuple(map(int, input().split()))

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))


for ele in b_list:

    if ele in a_list:
        flag = True
        index = a_list.index(ele)

        for i in range(n2):
            if b_list[i] != a_list[index + i]:
                flag = False
                break

    else:
        flag = False

    
if flag:
    print("Yes")

else:
    print("No")