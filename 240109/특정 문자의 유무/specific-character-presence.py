s = input()

a = "ee"
b = "ab"
a_same = False
b_same = False

for i in range(len(s) - 2 + 1):

    if s[i] == a[0] and not a_same:
        for j in range(len(a)):
            if s[i+j] != a[j]:
                a_same = False
                break
            a_same = True

    if s[i] == b[0] and not b_same:
        for i in range(len(b)):
            if s[i+j] != b[j]:
                b_same = False
                break
            b_same = True

if a_same:
    print("Yes", end=" ")
else:
    print("No", end=" ")

if b_same:
    print("Yes")
else:
    print("No")