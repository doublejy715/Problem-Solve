N = int(input())
dp = [i for i in range(N + 1)]

for i in range(1, N + 1):
    j = 1

    while j * j <= i:
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1

        j += 1

print(dp[N])


"""
시간초과난 코드
N = int(input())
dp = [_ for _ in range(N+1)]
for index in range(4,N+1):
    for i in range(index,0,-1):
        if index >= i**2:
            dp[index] = (1 + dp[index - i**2])
            break

print(dp[-1])
"""

