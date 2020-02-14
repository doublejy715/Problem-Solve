

def Merge(left,right):
    merged = list()
    left_pivot, right_pivot = 0,0

    while left_pivot < len(left) and right_pivot < len(right):
        if left[left_pivot] > right[right_pivot]:
            merged.append(right[right_pivot])
            right_pivot += 1
        else:
            merged.append(left[left_pivot])
            left_pivot += 1

    while left_pivot < len(left):
        merged.append(left[left_pivot])
        left_pivot += 1

    while right_pivot < len(right):
        merged.append(right[right_pivot])
        right_pivot += 1

    return merged


def Merge_Split(data):
    if len(data) == 1:
        return data
    left = Merge_Split(data[:int(len(data) / 2)])
    right = Merge_Split(data[int(len(data) / 2):])
    return Merge(left,right)


data = [4,7,2,68,23,95,0,14,3]

print(Merge_Split(data))