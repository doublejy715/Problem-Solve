document = input()
word = input()

index = 0
result = 0

# 올라가는 숫자를 linear하게 하지 못할 경우 이렇게 한다.(도중 과정을 뛰어넘고 싶을때 while)
while len(document) - index >= len(word):           # document를 벗어나지 않도록 구분
    if document[index:(index + len(word))] == word: # index 부터 word길이 만큼 비교 해서 일치하는지 확인
        result += 1
        index += len(word)                          # index를 길이만큼 이동한다.
    else:
        index += 1

print(result)

'''
data = list(input())
value = list(input())
count = 0
result = 0
for i in range(len(data)-len(value)):
    result1 = 0
    if count / len(value) != 0:
        count += 1
        continue
    if data[i] == value[0]:
        for j in range(len(value)):
            if data[i+j] == value[j]:
                result1 += 1
        if result1 == len(value):
            result += 1

print(result)
'''