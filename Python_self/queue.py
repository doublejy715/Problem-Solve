
data = list()

def enqueue(data):
    data.append(input())
    return data

def dequeue():
    value = data[0]
    del data[0]
    return value
