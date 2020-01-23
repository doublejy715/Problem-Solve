def selection_sort(data):
    for stand in range(len(data) - 1):  # data의 길이만큼 반복하여준다.
        lowest = stand
        for index in range(stand + 1, len(data)):  # 시작하는 것을 가장 작은것으로 생각하고 맨 마지막 까지 반복
            if data[lowest] > data[index]:  # 검사 & swap 하는 코드, 해당 숫자의 좌표를 저장하여준다.
                lowest = index # data[lowest] : 가장 작은 값이 있는 좌표, data[index] : lowest와 비교하려는 좌표
        data[lowest], data[stand] = data[stand], data[lowest]
    return data

data = [6,9,4,7,1]
selection_sort(data)
print(data)