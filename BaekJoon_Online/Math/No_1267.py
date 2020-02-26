N = int(input())
data = []
result = [['Y',0],['M',0]]
num = list(map(int,input().split()))
for i in num:
    result[1][1] += (i//60+1)*15
    result[0][1] += (i//30+1)*10
if result[1][1] > result[0][1]:
    print(*result[0],sep=' ')
elif result[1][1] == result[0][1]:
    print(result[0][0],result[1][0],result[0][1])
else:
    print(*result[1],sep=' ')