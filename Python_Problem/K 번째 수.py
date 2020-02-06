def merge(left,right):
    result = list()
    left_point, right_point = 0,0

    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            result.append(right[right_point])
            right_point += 1
        else:
            result.append(left[left_point])
            left_point += 1

    while len(left) > left_point:
        result.append(left[left_point])
        left_point += 1

    while len(right) > right_point:
        result.append(right[right_point])
        right_point += 1

    return result


def mergesplit(data):
    if len(data) <= 1:
        return data
    left = mergesplit(data[:int(len(data)/2)])
    right = mergesplit((data[int(len(data)/2):]))
    return merge(left,right)


result1 = list()
N,K = map(int,input().split(' '))
data = list(map(int,input().split(' ')))

result1 = mergesplit(data)
print(result1[K-1])