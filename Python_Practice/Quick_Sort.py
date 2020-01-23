# 단순하게 첫번째 맴버를 기준data로 하여 list내의 data를 구분하는 코드
def Quick_Sort_1(data):
    compare = data[0]
    del data[0]
    for index  in range(len(data)):
        if data[index] > compare:
            return data[:index]+[compare]+data[index:]
data_list = [4, 1, 2, 5, 7]
print(Quick_Sort_1(data_list))

def Quick_Sort_2(data):
    if len(data) <= 1:
        return data
    right, left = list(), list()
    pivot = data[0]
    for index in range(1,len(data)):
        if data[index] < pivot:
            left.append(data[index])
        else:
            right.append(data[index])
    return Quick_Sort_2(left) + [pivot] + Quick_Sort_2(right)

import random
data_list = random.sample(range(100), 10)
Quick_Sort_2(data_list)
print(data_list)
