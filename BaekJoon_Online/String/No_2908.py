def Num(number):
    h, t, z = number // 100, number % 100 // 10, number % 10
    return z*100 + t*10 + h

num = list(map(int,input().split()))
result = []
for number in num:
    result.append(Num(number))
print(max(result))