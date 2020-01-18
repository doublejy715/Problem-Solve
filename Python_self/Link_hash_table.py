'''
기본적 해시 함수에서 발생할 수 있는 일을 가정한다.
해시 함수의 key값이 동일하여 같은 위치에 '저장'해야 할 경우

기존의 해시 함수에서 수정할 생각을 하지 말고 새롭게 만든다고 생각한다.
(이미 해시 테이블엔 string의 키값이 [0]에, 키에대한 value가 [1]에 저장되는 구조이다.)
1. 링크 리스트를 이용해서 저장공간을 확보한다.

'''
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
    # 값이 하나이상 저장된 경우
    if hash_table[hash_address] != 0:
        # 기존의 value를 수정 해 주는 경우.
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        # 기존의 값들이 index_key가 존재하지 않는 경우 -> 새롭게 추가해 준다.
        hash_table[hash_address].append([index_key,value])
    #아예 처음 지정해 주는 경우
    else:
        hash_table[hash_address]=[[index_key,value]]


# 3. 불러오는 함수
def read_data(data):                    # 이것 역시 바뀌게 된다. 각 해쉬테이블의 index_key를 비교한다.
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    for index in range(len(hash_table[hash_address])):
        if hash_table[hash_address][index][0] == index_key:
            return hash_table[hash_address][index][1]
    return None