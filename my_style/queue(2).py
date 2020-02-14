data = list()
# 1. 삽입하는 기능
def enqueue(data,x):
    data.append(x)
    return data

# 2. 한가지 추출하는 기능
def dequeue(data):
    tmp = data[0]
    del data[0]
    return print(tmp)

enqueue(data,1)
enqueue(data,2)
enqueue(data,3)
enqueue(data,4)
print(data)
dequeue(data)
dequeue(data)
dequeue(data)
dequeue(data)