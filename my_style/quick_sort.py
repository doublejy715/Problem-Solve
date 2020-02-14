def Quick_Sort(data):
    if len(data) <= 1:
        return data

    left, right = [],[]
    pivot = data[0]

    for index in range(1,len(data)):
        if data[index] > pivot:
            right.append(data[index])
        else:
            left.append(data[index])

    return Quick_Sort(left) + [pivot] + Quick_Sort(right)

data = [4,7,2,68,23,95,0,14,3]

print(Quick_Sort(data))