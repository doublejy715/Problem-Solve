N = int(input())
result = []
for i in range(N):
    string = str(input())
    number = str()
    for index in range(len(string)):
        if len(string)-1 != index:
            if 47 < ord(string[index]) < 58:
                number = number + string[index]
            elif not 47 < ord(string[index]) < 58:
                if not number == '':
                    result.append(int(number))
                    number = str()
        else:
            if 47 < ord(string[index]) < 58:
                number = number + string[index]
                result.append(int(number))

print(*sorted(result),sep='\n')
