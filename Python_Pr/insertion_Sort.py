def Insertion_Sort(data):
    for index in range(len(data)-1):  # 차례대로 반복한다.
        for index2 in range(index+1,0,-1):  # index+1을 시작으로 하여 마지막까지 감소하며 검사한다, index2는 옴겨지는 숫자의 위치좌표 의미한다.
            if data[index2-1] > data[index2]:
                data[index2], data[index2-1] = data[index2-1],data[index2]
            else:
                break
    return data

data = [5,3,7,8,2,10]
Insertion_Sort(data)
print(data)
