# 10명 미만, 4과목 평균 > 60
# pass, fail
# 통과한 사람의 수

n = int(input())

cnt = 0
for _ in range(n):
    score_list = list(map(int, input().split()))

    sum_val = 0
    for score in score_list:
        sum_val += score
    
    avg = sum_val / len(score_list)

    if avg >= 60:
        print("pass")
        cnt += 1

    else:
        print("fail")

print(cnt)