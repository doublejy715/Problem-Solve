Stack_list=list()

def push(data): # Stack에 data를 밀어 넣는 함수
    Stack_list.append(data)

def pop(): # Stack에 data를 빼내는 함수
    print(Stack_list[-1])
    del Stack_list[-1]

# test 정의한 함수를 사용할 때는 대상을 적지 않아도 된다.(내부에 대상이 정해져 있으므로)
push(12)
push('abc')
push(2345)

pop()
pop()
pop()
