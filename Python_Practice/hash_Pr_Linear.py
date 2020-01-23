hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data,value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address,len(hash_table)): # 현재 위치 다음부터 끝까지 훑어본다
            if hash_table[index] == 0: # 만약에 비어있는 key 칸이 존재한다면 넣어준다.
                hash_table[index] = [index_key,value]
                return
            # 값을 업데이트 해 주는 경우
            elif hash_table[index][0] == index_key: #찾는 키가 일치하는 경우
                hash_table[index][1] = value
                return
            else:
                hash_table[hash_address] = [index_key,value]
    else:
        return None
# 값을 읽어오는경우
def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    # 만약 저장되어있는 경우면 key 일치 여부 검사를 시작한다.
    if hash_table[hash_address] != 0:
        for index in range(hash_address,len(hash_table)): # index_key와 일치하는 구간동안을 반복해 준다.
            if hash_table[index][0] == 0: # 만약 반복하는 동안에 0이 나오면 Key 의 일치 범위가 아니기 때문에 끝낸다.
                return None
            elif hash_table[hash_address][0] == hash_table[index]: # 일치하는 경우가 발생하면 해당 index의 값을 읽어온다.
                return hash_table[index][1]
    else:
        return None


