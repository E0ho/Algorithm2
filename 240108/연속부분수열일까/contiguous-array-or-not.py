n1, n2 = tuple(map(int, input().split()))

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))


for i in range(n1 - n2 + 1):

    flag = False
    if a_list[i] == b_list[0]:
        flag = True

        for j in range(n2):
            if a_list[j + i] != b_list[j]:
                flag = False

    if flag:
        break

if flag:
    print("Yes")
else:
    print("No")