# 피보나치 수열 -> 이전 두 항의 합
# DP -> 초기조건, 점화식

# 입력
n = int(input())

# 동적 계획법
dp = [0] * (n + 1)

# 초기 조건
dp[1] = 1
dp[2] = 1

for i in range(3, n + 1):
    dp[i] = dp[i-1] + dp[i-2]

if n == 1 or n == 2:
    print(1)
else:
    print(dp[n])