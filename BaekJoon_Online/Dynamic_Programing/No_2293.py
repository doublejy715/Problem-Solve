import sys
read = sys.stdin.readline

def Solve(por,coin):
    dp = [0 for _ in range(100001)]; dp[0]=1

    # coin의 가치를 뺸 나머지 경우는 dp[i-j]에 저장되어 있으므로 가져와서 더한다.
    for j in coin:
        for i in range(j,k+1):
            dp[i] += dp[i-j]

    return print(dp[k])



def Input():
    n,k = map(int,read().strip().split())
    coins = []
    for i in range(n):
        coins.append(int(read().strip()))

    return k,coins


k,coin = Input()
Solve(k,coin)