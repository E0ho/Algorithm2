n = int(input())

# 3의 배수 -> %3 == 0
# 100의 자리   -> 3, 6, 9 
# 10의 자리    -> 3, 6, 9 
# 1의 자리     -> 3, 6, 9 

for i in range(1, n+1):

    num = i

    while i > 10:
        # 1의 자리 검사
        check = i % 10
        if check % 3 == 0:
            num = 0
            break

        # 1의 자리 제거
        i = i // 10

    # 3의 배수
    if num % 3 == 0:
        num = 0

    print(num, end=" ")