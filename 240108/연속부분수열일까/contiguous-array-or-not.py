n1, n2 = tuple(map(int, input().split()))

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))


for i in range(n1):

    if a_list[i] == b_list[0]:
        flag = True
        for j in range(i, i + n2 + 1):
            if a_list[j] != b_list[j - i]:
                flag = False
                break

if flag:
    print("Yes")
else:
    print("No")