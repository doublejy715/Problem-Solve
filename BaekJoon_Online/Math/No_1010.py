num = int(input())
result = num
count = 0
while True:
    cal = num//10 + num%10
    num = num%10*10 + cal%10
    count += 1
    if num == result:
        break
print(count)