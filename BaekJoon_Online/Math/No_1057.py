N,K,I = map(int,input().split())
count = 0
while K != I:
    count += 1
    K = (K+1)//2
    I = (I+1)//2
print(count)