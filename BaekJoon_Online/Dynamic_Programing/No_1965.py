N = int(input())
data = list(map(int,input().split()))
Dp = [0 for _ in range(N)]

for i in range(N):
    d = []
    for j in range(i):
        if data[i] > data[j]:
            d.append(Dp[j]+1)
    if not d:
        Dp[i] = 1

    else:
        Dp[i] = max(d)
print(max(Dp))

"""
다른 방법이다.
import bisect as b
input()
s,l=[*map(int,input().split())],[]
for i in s:
    # 바로바로 완벽한 상자를 만들어 준다.
    # 상자 넣을 위치를 알려주는 것
    j=b.bisect_left(l,i)
    # 넣을 상자가 가장 큰 경우
    if j==len(l):
        l+=[i]
    # 수정할 경우
    else:l[j]=i
print(len(l))
"""