'''
List 형식으로 해시 함수를 만든다.
List 는 key 들이 숫자로 되어있기 때문에(위치를 따른다.) String을 숫자로 바꿔주는 Hashlib 를 이용한다.
해쉬 함수 : key % 8
해쉬 키 생성 : hash(data)
구성
1. 키를 얻는 함수 2. 저장하는 함수 3. 값을 읽어오는 함수
'''
import hashlib

hash_table = list([0 for i in range(10)])


# 1. 키를 얻는 함수 (키 : 찾으려는 string값을 해시 함수를 이용하여 키로 만든다)
def get_key(data):
    return hash(data)


# 2. 저장하는 함수
def save_data(data,value):
    key = get_key(data) % 10
    hash_table[key] = value


# 3. 불러오는 함수
def read_data(data):
    key = get_key(data) % 10
    return hash_table[key]


