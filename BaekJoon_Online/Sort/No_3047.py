num1,num2,num3 = map(int,input().split())
data = input()
A = min(num1,num2,num3)
C = max(num1,num2,num3)
B = (num1+num2+num3)-A-C
for _ in data:
    print(eval(_),end=' ')