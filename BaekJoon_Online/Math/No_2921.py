N = int(input())
memo = [1 for _ in range(N+1)]
if N >= 1:
    memo[1] = 3
if N >= 2:
    memo[2] = 12
for index in range(3,N+1):
    memo[index] = memo[index-1] + index*(index+1)*3//2
print(memo[N])