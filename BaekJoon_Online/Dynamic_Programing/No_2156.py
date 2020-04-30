# dp[i-1] 경우 생각 안함(현재의 와인을 마시지 않는 경우)
import sys
sys.setrecursionlimit(100001)

def Solve(n,wines):
    dp = []
    if n == 1:
        return print(wines[-1])
    if n == 2:
        return print(sum(wines))
    dp.append(wines[0]);dp.append(wines[0]+wines[1])
    if n >= 3:
        for i in range(2,n):
            if i == 2:
                dp.append(max(dp[1],dp[0]+wines[2],wines[1]+wines[2]))
            else:
                dp.append(max(dp[i-3]+wines[i-1]+wines[i],dp[i-2]+wines[i],dp[i-1]))
        return print(max(dp))

def Input():
    n = int(input())
    wine = []
    for i in range(n):
        wine.append(int(input()))

    return n, wine


number, wines = Input()
Solve(number,wines)