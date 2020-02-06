case , result = int(input()), list(map(int,input().split(' ')))
A = list()

for index in range(1,len(result)+1):
    A.append(index*result[index-1]-sum(A))

for i in A : print(i, end=' ')