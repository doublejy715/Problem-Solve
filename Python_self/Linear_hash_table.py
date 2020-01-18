hash_table = list([0 for i in range(10)])


# 1. 키를 얻는 함수 (키 : 찾으려는 string값을 해시 함수를 이용하여 키로 만든다)
def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 10


# 2. 저장하는 함수
def save_data(data,value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        # 기존의 value를 수정 해 주는 경우.
        if hash_table[hash_address][0] == index_key:
            hash_table[hash_address][1] = value
            return
        # hash_address가 일치하지만 index_key가 일치하지 않는 경우 밑에 빈 공간에 저장 해 준다.
        else:
            for index in range(hash_address,len(hash_table)):
                if hash_table[index][0] == 0:
                    hash_table[index][0] = [index_key,value]
                    return
    # 처음 저장하는 경우
    else:
        hash_table[hash_address] = [index_key,value]

# 3. 불러오는 함수
def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:                           # 해당 해시 어드레스에 값이 무엇인가가 있다면 찾아본다.
        for index in range(hash_address,len(hash_table)):
            if hash_table[index][0] == index_key:               # 밀린 데이터 중 일칠하는 index_key가 존재한다면 읽어온다.
                return hash_table[index][1]
            elif hash_table[index][0] == 0:                     # 찾아 봣는데 밀린 데이터가 없으면 없다고 표현
                return None
    else:
        return None

