n = int(input())

x = 0
while True:
    
    if n == 2 ** x:
        print(x)
        break

    x += 1