N, K = map(int,input().split())
coin = [int(input()) for _ in range(N)]
count, remain = 0, K
for i in range(len(coin)-1,-1,-1):
    count += remain // coin[i]
    remain = remain%coin[i]
print(count)