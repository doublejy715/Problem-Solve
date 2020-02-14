def selection_sort(data):
    for index1 in range(len(data)-1):
        lowest = index1
        # 가장 작은것을 찾아낸다.
        for index2 in range(index1,len(data)):
            if data[lowest] > data[index2]:
                lowest = index2
        # 가장 작은것과 기준점을 교환해 준다.
        data[lowest], data[index1] = data[index1],data[lowest]

    return data

data = [4,7,2,68,23,95,0,14,3]

print(selection_sort(data))