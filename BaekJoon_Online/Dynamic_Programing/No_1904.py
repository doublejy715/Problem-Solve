n = int(input())
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    Dp = [0 for i in range(n+1)]; Dp[1],Dp[2]=1,2

    for i in range(3,n+1):
        Dp[i] = (Dp[i-2]+Dp[i-1])%15746

    print(Dp[-1])