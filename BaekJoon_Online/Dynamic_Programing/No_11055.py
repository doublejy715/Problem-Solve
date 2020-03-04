N = int(input())
data = list(map(int,input().split()))
Dp = [data[i] for i in range(N)] 
# 깊은 복사와 얉은 복사를 주의해서 활용한다. 
# 그냥 Dp=Data하면 얕은 복사이므로 주소값만 받아와, Data가 수정되면 Dp도 자동으로 수정된다.

for i in range(N):
    for j in range(i):
        if data[i] > data[j] and Dp[i] < Dp[j] + data[i]:
            Dp[i] = Dp[j] + data[i]

print(max(Dp))

"""
더 빠른 방법

n = int(input())
a = list(map(int, input().split()))
c = [0] * 1001
for i in range(n): c[a[i]] = max(c[:a[i]]) + a[i] # 해당 숫자까지 가는데 필요한 총 수의 합(누적 합)
print(max(c))
"""