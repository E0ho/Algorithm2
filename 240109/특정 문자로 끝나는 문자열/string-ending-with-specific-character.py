li = [
    input()
    for _ in range(10)
]

c = input()

for ele in li:
    if ele[-1] == c:
        print(ele)