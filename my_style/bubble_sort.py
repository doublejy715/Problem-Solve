def Bubble_Sort(data):
    for index1 in range(len(data)-1):
        swap = False
        for index2 in range(len(data) - index1 - 1):
            if data[index2] > data[index2+1]:
                data[index2], data[index2+1] = data[index2+1],data[index2]
                swap = True
        if not swap:
            break
    return data


data = [7,2,9,12,54,23,72,0]

print(Bubble_Sort(data))