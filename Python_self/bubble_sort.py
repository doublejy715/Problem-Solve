'''
버블정렬: 두

'''
data = [4,7,1,3,2,8]
def bubble_sort(data):
    for index1 in range(len(data)-1):
        for index2 in range(len(data)-index1-1):
            if data[index2] > data[index2+1]:
                data[index2],data[index2+1] = data[index2+1],data[index2]

    return data

bubble_sort(data)
print(data)