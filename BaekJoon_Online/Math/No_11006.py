T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    for i in range(0,M+1):
        if M+i == N:
            print(M-i,i,sep=' ')