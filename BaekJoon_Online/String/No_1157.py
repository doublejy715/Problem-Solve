string = input()
alpa = [0 for _ in range(26)]
for index in range(len(string)):
    if 97 <= ord(string[index]) <= 122:
        alpa[ord(string[index])-97] += 1
    else:
        alpa[ord(string[index])-65] += 1

count = 0
for i in range(len(alpa)):
    if max(alpa) == alpa[i]:
        count += 1
if count > 1:
    print("?")
else:
    print(chr(alpa.index(max(alpa))+65))