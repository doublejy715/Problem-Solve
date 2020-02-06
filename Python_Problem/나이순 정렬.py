N = int(input())
data = []

for i in range(N):
    age, name = input().split(' ')
    age = int(age)
    data.append([age,name])

for i in range(1,201):
    for _ in range(N):
        if data[_][0] == i:
            print(data[_][0],data[_][1])
