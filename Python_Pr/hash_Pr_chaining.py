hash_table = list(0 for i in range(0,8))
# 리스트 변수를 이용하여 hash_table 구현하여 보기
# chaining은 리스트 함수를 이용하여 구현한다.
def get_key(data):
    return hash(data)


# hash화된 data을 이용하여 테이블 저장위치를 지정하여준다.
def hash_function(key):
    return key % 8


# 해쉬 테이블에 값을 저장하여주는 정의
def save_data(data, value):
    index_key = get_key(data) # 중복 방지를 위
    hash_address = hash_function(get_key(data))  # data의 해쉬를 통해서 list의 위치를 얻는다
    if hash_table[hash_address]!=0: # 만약에 hash_address 위치에 값이 존재한다고 한다면
        for index in range(len(hash_table[hash_address])): # 해당 해시 테이블 값에 존재하는 링크된 데이터 길이만큼 반복한다.
            if hash_table[hash_address][index][0] == index_key: # 현재 테이블에 존재하는 데이터의 키가 찾고자 하는 key랑 일치한다면
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key,value]) # 현재 저장된 키랑 같은 데이터가 없다면 뒤에 추가한다. ()안에 어떻게 넣을지 List 형태로 지정한다.
    else:
        hash_table[hash_address] = [[index_key,value]]# 만약에 hash_address 위치에 값이 아무것도 존재하지 않으면

#해쉬 테이블에 있는 value를 읽어오는 정의
def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address]!=0:
        for index in range(len(hash_table[hash_address])):
          if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
    else: # 없으면 없는걸로 리턴한다.
        return None

save_data('Dd', '1201023010')
save_data('Data', '3301023010')