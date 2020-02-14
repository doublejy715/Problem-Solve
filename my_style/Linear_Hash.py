# Linear Probing 기법으로 저장하기

hash_table = list([0 for _ in range(8)])


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

    if hash_table[index] == 0:
        hash_table[index] = [hash_value, value]

    else:
        for index1 in range(index, len(hash_table)):
            if hash_table[index1] == 0:
                hash_table[index1] = [hash_value, value]
                return
            elif hash_table[index1][0] == hash_value:
                hash_table[index1][1] = value
                return


# 4. data 읽어오기
def read_data(key):
    hash_value = get_hashvalue(key)
    index = hashtoindex(hash_value)

    if hash_value[index] != 0:  # 왜 오류나지???
        for index1 in range(index, len(hash_table)):
            if hash_table[index1][0] == hash_value:
                return hash_table[index1][1]
            elif hash_talbe[index1][0] == 0:
                return None
        return None
    else:
        return None