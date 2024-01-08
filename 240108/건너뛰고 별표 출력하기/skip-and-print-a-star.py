n = int(input())

# cnt = 1
# for i in range(1, 2*n):
#     print("*" * cnt, end="")
#     print()
#     print()
#     if i < n:
#         cnt += 1

#     else:
#         cnt -= 1
    
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()
    print()

for i in range(n-1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
    print()