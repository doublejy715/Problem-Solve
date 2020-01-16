# hash table 만들기

hash_table = list([i for i in range(0,10)]) # 0~10까지 키를 가지고 각 키마다 0~9까지의 값을 가진 리스트가 형성된다.
print(hash_table)


# key를 만들어 주는 정의
def hash_func(key):  # 가장 간단한 나누기 해쉬 이용
    return key % 5


# 해쉬 테이블에 값을 저장하는 함수(data : 찾으려는 키 변환전 값, value : 값 입력 대상)
def storage_data(data,value):
    key = ord(data[0])
    hash_address = hash_func(key)
    list[hash_address] = value


# 해쉬 테이블에 있는 value를 가져오는 함수(key가 아닌 data값을 가지고 한다)
def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return print(list[hash_address])
