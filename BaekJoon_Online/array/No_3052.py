count = [0 for _ in range(42)]
data = [ int(input()) for _ in range(10)]
result  = 0
for index in data:
    count[index%42] = 1
for index in count:
    if index == 1:
        result += 1
print(result)