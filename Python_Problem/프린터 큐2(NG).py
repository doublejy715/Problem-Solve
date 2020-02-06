test_case = int(input())

for i in range(test_case):
    count = 0
    N, M = map(int,input().split(' '))
    data = list(map(int, input().split(' ')))
    target = data[M]
    while True:
        if data[0] == max(data):
            count += 1
            if data[0] == target:
                print(count)
                break
            else:
                data.pop(0)
        else:
            data.append(data.pop(0))



'''
test_case = int(input())


for i in range(test_case):
    N, M = list(map(int,input().split(' ')))
    data = list(map(int, input().split(' ')))
    data = [(i,idx) for idx,i in enumerate(data)] # 데이터를 튜플형식으로 저장이 가능하다 (data1:0)(data2:1)(data3:2)...
    while True:                                   # 위의 코드와 비교했을 때 중복되는 중요도가 발생할 시 올바른 위치 구분 어려움 그러므로 튜플형식 필요
        count = 0
        if data[0][0] == max(data)[0]:        # 어떻게 쓰는지 모름
            count += 1
            if data[0][0] == M:
                print(count)
                break
            else:
                data.pop(0)
        else:
            data.append(data.pop(0))
'''