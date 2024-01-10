n = int(input())

grid = [
    int(input())
    for _ in range(n)
]

length = n

def cut(s, e):
    global length, grid
    temp = []

    for i in range(length):
        if s < i or e > (i + 1):
            temp.append(grid[i])
        
    length = len(temp)
    for i in range(length):
        grid[i] = temp[i]


for _ in range(2):
    s, e = tuple(map(int, input().split()))
    s = n - s
    e = n - e

    cut (s, e)


print(length)
for i in range(length):
    print(grid[i])