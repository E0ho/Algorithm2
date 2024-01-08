n1, n2 = tuple(map(int, input().split()))

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))


for i in range(n1):
# 9 2 4 1 3 3 1 4 6 8
#     4 1 3 3 1 4
    if a_list[i] == b_list[0]:
        flag = True
        for j in range(n2):
            if a_list[i+j] != b_list[j]:
                flag = False
                break
            else:
                pass
    
    else:
        flag = False

if flag:
    print("Yes")
else:
    print("No")