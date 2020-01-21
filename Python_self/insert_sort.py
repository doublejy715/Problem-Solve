'''
"삽입정렬"
1. 리스트의 가장 앞의 것을 기준인 key로 잡고, 뒤로 이동시키면서 값을 비교한다.
2. 비교하는 값이 key보다 작은 경우 : 앞에 정렬되어있던 숫자들과도 크기를 비교해서 정렬시킨다.
3. 비교하는 값이 key보다 큰 경우 : 이때까지의 key를 다음칸으로 바꾼다. 이후 계속해서 비교한다.
key가 처음부터 끝까지 이동하게 되면 정렬이 완성되게 된다.
그런데 여기서는 다음과 같이 정렬한다.
1. 리스트를 처음부터 끝까지 선택하여간다.
2. 하나를 선택하면 그 뒤에 있는 숫자를 선택한다.
3. 선택한 숫자가 key랑 비교하여 큰 경우는 그냥 넘어간다.
4. 선택한 숫자가 작은경우는 key랑 위치를 바꾸고 앞에서 정렬한다.

생각해 보니깐 key를 하나 정하고 그 밑에 있는건 정렬만 해도 끝난다.
그렇기 때문에 key를 하나씩 정하는 함수 for 1개, 밑의 숫자들을 정렬하기 위한 for문 1개로 할 수 있다.
'''

data = [6,4,8,13,1,3,7,16]
def insert_sort(data):
    for index1 in range(1,len(data)):                     # 키를 하나씩 옮기기 위한 용도
        for index2 in range(index1, 0, -1):          #
            if data[index2] < data[index2-1]:
                data[index2], data[index2-1] = data[index2-1],data[index2]
            else:
                break
    return data

print(insert_sort(data))
