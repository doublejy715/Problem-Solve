# push, pop, top, Isempty의 기능 정의
def push(data,x):
    data.append(x)
    return data

def pop(data):
    tmp = data[-1]
    del data[-1]
    return tmp

def top(data):
    return data[-1]

def Isempty(data):
    if len(data) == 0:
        return True
    else:
        return False

# 리스트의 형성
data = list()

print(Isempty(data))
push(data,1)
push(data,2)
push(data,3)
push(data,4)
print(data)
pop(data)
print(top(data))
print(Isempty(data))
print(pop(data))
print(pop(data))