'''
1. 아스키 값을 이용해서 더 쉽게 할 수 있다.(ord)
2. 반복하는 것은 단순하게 앞문자에서 뒤문자를 더하고 맨 처음의 것을 빼 줌으로써 간단하게 해결 할 수 있다.
3. print("{}%".format()) 으로 출력할 형태를 지정 가능하다 (좀 더 자세하게)
'''

a,b = map(int,input().split(' '))
name_a , name_b = list(map(str,input().split(' ')))
num_a, num_b = list(),list()
al = {
    'A':3,'B':2,'C':1,'D':2,'E':4,'F':3,'G':1,'H':3,'I':1,'J':1,'K':3,'L':1,'M':3,'N':2,'O':1,'P':2,'Q':2,'R':2,'S':1,'T':2,'U':1,'V':1,'W':1,'X':2,'Y':2,'Z':1
}
for index1 in name_a:
    num_a.append(al[index1])
for index2 in name_b:
    num_b.append(al[index2])

result = list()
for index3 in range(a+b):
    if len(num_a) == 0:
        for index4 in range(len(num_b)):
            result.append(num_b[index4])
        break
    elif len(num_b) == 0:
        for index4 in range(len(num_a)):
            result.append(num_a[index4])

        break
    elif index3 % 2 == 0 :
        result.append(num_a.pop(0))
    elif index3 % 2 == 1:
        result.append(num_b.pop(0))

result1 = list()
while len(result1) != 2:
    for index1 in range(len(result)-1):
        result1.append((result[index1] + result[index1+1]) % 10)
    result = result1