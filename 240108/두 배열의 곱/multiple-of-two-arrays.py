li1 = [
    list(map(int, input().split()))
    for i in range(3)
]

input()

li2 = [
    list(map(int,input().split()))
    for i in range(3)
]

result = [
    [0] * 3
    for i in range(3)
]
for i in range(3):
    for j in range(3):
        result[i][j] = li1[i][j] * li2[i][j]

for i in range(3):
    for j in range(3):
        print(result[i][j], end=" ")
    print()