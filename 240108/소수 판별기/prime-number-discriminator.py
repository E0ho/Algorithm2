n = int(input())

bo = True
for i in range(2, n):
    if n % i == 0:
        print("C")
        bo = False
        break

if bo:
    print("P")