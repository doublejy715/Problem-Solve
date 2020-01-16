# 어떤 데이터리스트가 있을 때 리스트를 앞뒤로 짜르는 코드 작성해보기 (일반화)
def practice1(list):
    left =list[:int(len(list)/2)]
    right = list[int(len(list) / 2):]
    return left,right

# mergesplit 에 의해서 하나로 된 부분을 다시 정렬하면서 합치는 과정을 나타낸다.
# idea 는 left와 right의  숫자를 비교하여 정렬한다. 포인트를 이용한다
def merge(left,right):
    merged = list()
    left_point,right_point = 0,0

    # 경우를 구별해 줘야한다.
    # case1. left,right에 둘다 숫자가 존재할 경우
    while len(left) > left_point and len(right) > right_point: # 밑에서 계속 point의 숫자가 커지므로 범위를 넘어갈때까지 게속 반복한다.
        if left[left_point] > right[right_point]:  # 왼쪽의 값이 더 큰 경우 오른쪽의 값을 넣어준다.
            merged.append(right[right_point])
            right_point += 1
        elif left[left_point] < right[right_point]:  # 오른쪽의 값이 더 큰 경우 왼쪽의 값을 넣어준다.
            merged.append(left[left_point])
            left_point += 1

    # case2. right에만 숫자가 존재하는 경우 나눠질때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    # case3. left에만 숫자가 존재하는 경우 나눠질때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    return merged

# 재귀함수를 이용한 리스트 분리, 코드
# 이 함수를 이용하면 결국 list의 길이는 1개로  나오게 된다.
def mergesplit(list):
    if len(list) <= 1:
        return list
    middle = int(len(list)/2)
    left = mergesplit(list[:middle])  # 이렇게 되면 계속해서 왼쪽에 있는 list들은 중앙을 기준으로 해서 길이가 1이 될때까지 잘라지게 된다.
    right = mergesplit(list[middle:])
    return merge(left,right)

