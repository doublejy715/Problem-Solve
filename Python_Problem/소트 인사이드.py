'''
병합 정렬로 해야된다.
1초당 5천만이 최대 데이터 처리수 이고, 문제에서 2초 준다고 했으므로 최대 1억까지 커버 가능
문제에서 최대 1억이라 했으므로 시간복잡도 O(N)을 이용해야 한다.
'''

def merge(left,right):
    merged = list()
    left_spot = 0
    right_spot = 0
    while len(left) > left_spot and len(right) > right_spot:
        if left[left_spot] >= right[right_spot]:
            merged.append(right[right_spot])
            right_spot += 1
        else:
            merged.append(left[left_spot])
            left_spot += 1

    while len(left) > left_spot:
        merged.append(left[left_spot])
        left_spot += 1

    while len(right) > right_spot:
        merged.append(right[right_spot])
        right_spot += 1

    return merged

def split(data):
    if len(data) <= 1:
        return data
    mid = int(len(data) /2)
    left = split(data[:mid])
    right = split(data[mid:])
    return merge(left, right)


data = list(map(int,input()))
result = split(data)
result = list(reversed(result))
for index in range(len(result)):
    print(result[index], end='')


