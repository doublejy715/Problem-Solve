
# 입력이 2개일 때 bubble_sort
def Bubble_Sort_2(data):
    if data[0] > data[1]:
        data[0], data[1] = data[1], data[0] # 스왑하는 코드이다.


def Bubble_Sort_3(data):
    count =0
    for index in range(0,len(data)-1-count):
        if data[index] > data[index+1]:
            data[index], data[index+1] = data[index+1], data[index]
        ++count


def bubblesort(data):
    for index in range(len(data) - 1):  # 몇번 반복하는가
        swap = False
        for index2 in range(len(data) - index - 1):  # 얼마만큼 조건을 체크해야 하는가
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True  # 여기서는 그냥 True로 해줌

        if swap == False:  # 만약 data 이미 정렬되어있는경우 판단도구
            break
    return data

import random

data1 = [5,1,3,7,6]
data_list = random.sample(range(100), 50)
print (bubblesort(data_list))
print (Bubble_Sort_3(data1))