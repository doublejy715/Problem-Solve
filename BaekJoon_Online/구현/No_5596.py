data1,data2 = [], []
data1 = list(map(int,input().split()))
data2 = list(map(int,input().split()))
print(max(sum(data1),sum(data2)))