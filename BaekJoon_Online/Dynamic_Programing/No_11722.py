N = int(input())
Data = list(map(int,input().split()))
Dp = [1 for _ in range(N)]

for i in range(N):
    count = 0
    for j in range(i):
        if Data[i] < Data[j]:
            # 가장 큰 Data[j]의 Dp값에서 1 더해준다.
            count = max(count,Dp[j])
    Dp[i] = count + 1

print(max(Dp))