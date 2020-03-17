data = input()
number = [0 for _ in range(26)]
for i in data:
    number[ord(i)-97] += 1
print(*number,sep=" ")