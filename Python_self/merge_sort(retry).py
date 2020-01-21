
'''
1. 함수를 생각하고 학 함수의 역할을 먼저 생각해 준다.
2. 먼저 함수 이름과 매개변수를 각각 적어준다.
3. 이후 return이 어떤것이 적합한지 생각해 본다.
'''
import random


def merge(left, right):                               # merge는 merge_split에 의해서 나눠진 list를 다시 합해준다.
    merged = list()
    key_l, key_r = 0, 0
    # 여기서 케이스를 나눈다. left와 right의 내용물이 있는가 또는 없는가에 따라서 결정한다.
    # 1. left, right 둘 다 내용물이 존재하는 경우
    while len(left) > key_l and len(right) > key_r:
        if left[key_l] > right[key_r]:
            merged.append(right[key_r])
            key_r += 1
        else:
            merged.append(left[key_l])
            key_l += 1

    # 2. right의 내용물이 존재하지 않는 경우(right가 옳은지 확인 해야됨!)
    while len(left) > key_l:
        merged.append(left[key_l])
        key_l += 1

    # 3. left의 내용물이 존재하지 않는 경우
    while len(right) > key_r:
        merged.append(right[key_r])
        key_r += 1
    return merged


def merge_split(data):                                      # merge_split은 들어온 리스트를 길이가 1이 될 때까지 나누어준다.
    mid = int(len(data)/2)
    if mid < 1:
        return data
    left = data[:mid]
    right = data[mid:]
    return merge(left,right)


data_list = random.sample(range(100),10)
print(data_list)
print(merge_split(data_list))