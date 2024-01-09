# A -> Run-length encoding
# 연속된 문자 -> 개수로 표현

a = input()

temp = a[0]
result = ""
cnt = 0

for i in range(len(a)):

    if temp != a[i]:
        result += temp + str(cnt)
        temp = a[i]
        cnt = 1

    else:
        cnt += 1

result += temp + str(cnt)

print(len(result))
print(result)