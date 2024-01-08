n = int(input())

# 3의 배수 -> %3 == 0
# 1의 자리
# 10의 자리
# 100의 자리

for i in range(1, n+1):
    if i % 3 == 0:
        print(0, end=" ")

    elif i > 10 and i % 10 % 3 == 0:
        print(0, end=" ")
    
    elif i > 10 and i // 10 % 3 == 0:
        print(0, end=" ")

    else:
        print(i, end=" ")