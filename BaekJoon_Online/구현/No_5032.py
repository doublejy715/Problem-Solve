count = 0
def Con(num,c):
    global count
    if num < c:
        return 0
    else:
        count += num//c
        return Con(num//c+num%c,c)

e,f,c = map(int,input().split())
num = e + f
Con(num,c)
print(count)