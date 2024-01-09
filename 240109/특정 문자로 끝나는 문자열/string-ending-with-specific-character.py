li = [
    input()
    for _ in range(10)
]

c = input()

bo = True
for ele in li:
    if ele[-1] == c:
        print(ele)
        bo = False

if bo:
    print("None")