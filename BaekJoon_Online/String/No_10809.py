string = input()
alpa = [-1 for _ in range(26)]
for index in range(len(string)):
    if alpa[ord(string[index])-97] == -1:
        alpa[ord(string[index])-97]=index
print(*alpa,sep=' ')