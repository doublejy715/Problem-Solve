# FIFO 형식 큐 설정하기

queue_list=list() # list로 저장할 공간을 지정하여 놓는다.

def enqueue(data): # queue_list에 넣기
    queue_list.append(data)

def dequeue(): # queue_list에서 정보 빼기
    if queue_list[0] == '\0':
        return False
    print(queue_list[0])
    del queue_list[0]

# test=
for index in range(2):
    for index2 in range(3):
        enqueue(index+3)

for index in range(2):
    for index2 in range(2):
        dequeue()

print(len(queue_list))