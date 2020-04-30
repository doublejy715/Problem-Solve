# 피보나치 관련있다.
def Solve(n):
    if n == 1 or n == 2:
        return print(1)
    else:
        dp = [1,1]
        for i in range(2,n):
            dp.append(dp[i-1] + dp[i-2])
        return print(dp[-1])

number = int(input())
Solve(number)