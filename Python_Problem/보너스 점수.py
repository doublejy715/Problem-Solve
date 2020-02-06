


pro = int(input())
data = input()
bonus = 0
result = 0

for index in range(pro):
    if data[index] == 'O':
        result += index+1+bonus             # 더 최적화 하면 result, bonus = result+index+1+bonus, bonus + 1로 줄이기 가능
        bonus += 1
    else:
        bonus = 0

print(result)
