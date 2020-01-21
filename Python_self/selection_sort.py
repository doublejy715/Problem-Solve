data = [8,5,2,6,9,3,1,4,0,7]

def selection_sort(data):
    for index1 in range(len(data)):
        min1 = index1
        for index2 in range(index1, len(data)):
            if data[min1] > data[index2]:
                min1 = index2                                # 최소 값의 좌표를 찾는다.
        data[min1],data[index1] = data[index1], data[min1]   # swap
    return data

print(selection_sort(data))

