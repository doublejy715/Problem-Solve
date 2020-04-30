# 더 좋게 하는 방법은?
def Solve(lens,datas):
    if lens == 1:
        return print(datas[-1])
    else:
        dp = [datas[0]]
        result = datas[0]
        for i in range(1,lens):
            dp.append(max(dp[i-1]+datas[i],datas[i]))
            result = max(result,dp[i])
        return print(result)


n = int(input())
data = list(map(int,input().split()))

Solve(n,data)