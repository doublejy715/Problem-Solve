mo = ['a','e','i','o','u']
string = input()
result = 0
for i in string:
    if i in mo:
        result += 1
print(result)