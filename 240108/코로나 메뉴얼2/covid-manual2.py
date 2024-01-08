# A - Y, 37
# B - N, 37
# C - Y, 36
# D - N, 36

# 3명씩 검사 -> 2명 이상 A -> E

m_list = list()

a = list(input().split())
b = list(input().split())
c = list(input().split())

a[1] = int(a[1])
b[1] = int(b[1])
c[1] = int(c[1])

m_list.append(a)
m_list.append(b)
m_list.append(c)

# a, b, c, d
count_list = [0] * 4

for ele in m_list:
    if ele[0] == "Y":
        if ele[1] >= 37:
            count_list[0] += 1
        else:
            count_list[2] += 1

    else:
        if ele[1] >= 37:
            count_list[1] += 1
        else:
            count_list[3] += 1

for ele in count_list:
    print(ele, end=" ")
    
if count_list[0] >= 2:
    print("E")