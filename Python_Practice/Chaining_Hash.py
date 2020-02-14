# Chaining 기법으로 충돌 해결하기
import hashlib

hash_table = list(0 for _ in range(8))


# 1. 해쉬 값 얻기
def get_hashvalue(key):
    return hash(key)


# 2. index 형성
def hashtoindex(hash_key):
    return hash_key % 8


# 3. data 형성
def save_data(key, value):
    hash_value = get_hashvalue(key)
    index = hashtoindex(hash_value)
    # 만약 저장되어 있지 않는다면
    if hash_talbe[index] == 0:
        hash_table[index] = [[hash_value, value]]
    else:
        for index1 in range(len(hash_table[index])):
            # 기존 저장된 값을 update 할 때
            if hash_table[index][index1][0] == hash_value:
                hash_table[index][index1][1] = value
                return
        # 기존 저장된 값이 없을 때
        hash_table[index].append([hash_value, value])


# 4. data 읽어오기
def read_data(key):
    hash_value = get_hashvalue(key)
    index = hashtoindex(hash_value)

    # 목록에 존재하지 않을때, 할때 검색 으로 나뉜다.
    if len(hash_table[index]) != 0:
        for index1 in range(len(hash_table[index])):
            if hash_table[index][index1][0] == hash_value:
                return hash_table[index][index1][1]
        return None
    else:
        return None