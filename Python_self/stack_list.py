stack_list = list()

# data는 넣고자 하는 데이터
def push(data):
    stack_list.append(data)


# pop은 꺼내주기만 하면 되므로 매개변수 없다.
def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data