N = int(input())
dp = [0 for _ in range(1001)]
dp[1], dp[2] = 1, 3
if N >= 3:
    for i in range(3,N+1):
         dp[i] = (2*dp[i-2] + dp[i-1])%10007
print(dp[N])