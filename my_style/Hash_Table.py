hash_table = list(0 for i in range(8))

# 가장 기본적인 기능 1.해쉬 값 얻기 2.저장할 수 있도록 index형성하기 3. data 저장하기 4. data 읽어오기
# 1. 해쉬 값 얻기
def get_hashvalue(key):
  return hash(key)

# 2. index 형성
def hashtoindex(hash_key):
  return hash_key % 8

# 3. data 형성
def save_data(key,value):
  index = hashtoindex(get_hashvalue(key))
  hash_table[index] = value

# 4. data 읽어오기
def read_data(key):
  index = hashtoindex(get_hashvalue(key))
  return hash_table[index]

save_data('banana','1000')
save_data('peach','2000')
save_data('포도','500')
print(read_data('banana'))
