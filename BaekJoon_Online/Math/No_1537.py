def Rev(num):
    num=str(num)[::-1]
    num = list(num)
    result = str()
    while True:
        if num[0] == '0':
            del num[0]
        else:
            break
    for i in num:
        result = result + i
    return int(result)

X, Y = map(int,input().split())

print(Rev(Rev(X)+Rev(Y)))