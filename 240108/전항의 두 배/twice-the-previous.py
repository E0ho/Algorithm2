a_list = list(map(int, input().split()))

for i in range(2, 10):
    a_list.append(a_list[i - 1] + 2 * a_list[i - 2])

for ele in a_list:
    print(ele, end=" ")