hash_table = list(0 for i in range(0,8))
# 리스트 변수를 이용하여 hash_table 구현하여 보기
# 위치를 찾고자 하는 data의 키를 hash함수를 통해서 얻어낸다.(키는 해시함수화 된 data 이다.)
def get_key(data):
    return hash(data)


# hash화된 data을 이용하여 테이블 저장위치를 지정하여준다.
def hash_function(key):
    return key % 8


# 해쉬 테이블에 값을 저장하여주는 정의
def save_data(data, value):
    hash_address = hash_function(get_key(data))  # data의 해쉬를 통해서 list의 위치를 얻는다
    hash_table[hash_address] = value

#해쉬 테이블에 있는 value를 읽어오는 정의
def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]
