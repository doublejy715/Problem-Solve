N, k = map(int,input().split(' '))
data = list()

for _ in range(N):
    W, V = map(int,input().split(' '))
    data.append([W,V])

data = sorted(data,key=lambda x:x[1]/x[0],reverse=True)
total_value = 0

for data1 in data:
    if data1[0] < k:
        total_value += data1[1]
        k -= data1[0]
    else:
        last = k / data1[0]
        total_value += int(last*data1[1])
        break

print(total_value)


'''
문제풀이 부분과 이론설명하는 부분의 차이를 알아보자

'''
