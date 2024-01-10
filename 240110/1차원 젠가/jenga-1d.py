n = int(input())

grid = [
    int(input())
    for _ in range(n)
]

length = n

def cut_array(s, e):
    temp = []
    global length, grid

    for i in range(length):
        if i < s or i > e:
            temp.append(grid[i])

    length = len(temp)

    for i in range(length):
        grid[i] = temp[i]


for _ in range(2):
    s, e = tuple(map(int, input().split()))

    # n번째 -> n Index
    s -= 1
    e -= 1

    cut_array(s, e)

print(length)
for i in range(length):
    print(grid[i])