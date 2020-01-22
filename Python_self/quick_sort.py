'''
첫번째 Data를 pivot이라 지정한 뒤 이것을 가지고 비교한다.

'''


def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left,right = list(),list()

    for index in range(1,len(data)):
        if data[index] < pivot:
            left.append(data[index])
        else:
            right.append(data[index])
    return quick_sort(left) + [pivot] + quick_sort(right)


data = [2,20,35,39,49,51,57,74,82,94]
print(quick_sort(data))