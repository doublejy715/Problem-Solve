N = int(input())
Dp = [0]* 101
Dp[1],Dp[2],Dp[3],Dp[4],Dp[5] = 1,1,1,2,2

for index in range(6,101):
    Dp[index] = min(Dp[index-5:index]) + max(Dp[index-5:index])

for i in range(N):
    num = int(input())
    print(Dp[num])