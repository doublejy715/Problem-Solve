price = 0
X,Y = map(float,input().split())
price = X/Y*1000
N = int(input())
for i in range(N):
    x, y = map(float, input().split())
    price = min(price,x/y*1000)

print(round(price,2))