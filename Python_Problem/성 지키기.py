N,M = map(int,input().split(' '))
data,Y,X = list(),list(),list()
for index in range(N):
    data.append(input())

for index1 in range(N):
    if 'X' not in data[index1]:
        X.append(index1)


for index2 in range(M):
    cap = False
    for index3 in range(N):
        if data[index3][index2] == 'X':
            cap = True
    if cap == False:
        Y.append(index2)


print(max(len(X),len(Y))) # 왜 둘중에 큰것만 세도 될까? 시뮬레이션을 통해서 규칙을 알아 낼 수 있다.