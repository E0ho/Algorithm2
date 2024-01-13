from collections import deque

n = int(input())
d = deque()

for i in range(1, n+1):
    d.append(i)

while d:
    d.popleft()
    if len(d) == 1:
        break
    d.append(d.popleft())



print(d[0])