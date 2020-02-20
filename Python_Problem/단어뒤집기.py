import sys


input = sys.stdin.readline
result = ''
inputs = input().splitlines()
print(inputs)
print(inputs[0])

"""s, tmp = input(), ""

ck = False
ans = ""

for i in s:
    if i == ' ':
        if not ck:
            ans += tmp[::-1] + " "
            tmp = ""
        else:
            ans += " "

    elif i == '<':
        ck = True
        ans += tmp[::-1] + "<"
        tmp = ""
    elif i == '>':
        ck = False
        ans += '>'
    else:
        if ck:
            ans += i
        else:
            tmp += i

ans += tmp[::-1]
print(ans)"""