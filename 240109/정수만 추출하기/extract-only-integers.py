a, b = input().split()

a_result = ""
b_result = ""

for i in a:
    if i.isdigit():
        a_result += i
    else:
        break


for i in b:
    if i.isdigit():
        b_result += i
    else:
        break


print(int(a_result) + int(b_result))