N = int(input())
data = list()
result = list()


def quick_sort(data):
    if len(data) <= 1:
        return data
    left = list()
    right = list()
    pivot = data[0]


    for j in range(1,len(data)):
        if data[j] > pivot:
            right.append(data[j])
        else:
            left.append(data[j])
    return quick_sort(left) + [pivot] + quick_sort(right)

def merge(left,right):
    merged = list()
    left_pivot,right_pivot = 0,0

    while len(left) > left_pivot and len(right) > right_pivot:
        if left[left_pivot] > right[right_pivot]:
            merged.append(right[right_pivot])
            right_pivot += 1
        else:
            merged.append(left[left_pivot])
            left_pivot += 1

    while len(left) > left_pivot:
        merged.append(left[left_pivot])
        left_pivot += 1

    while len(right) > right_pivot:
        merged.append(right[right_pivot])
        right_pivot += 1

    return merged


def mergesplit(data):
    if len(data) <= 1:
        return data
    left = mergesplit(data[:int(len(data)/2)])
    right = mergesplit(data[int(len(data)/2):])
    return merge(left,right)

for i in range(N):
    data.append(int(input()))


result = mergesplit(data)
for i in range(len(data)):
    print(result[i])