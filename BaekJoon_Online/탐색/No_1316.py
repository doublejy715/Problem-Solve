N = int(input())
count = 0
for _ in range(N):
    data = input()
    al = [0 for _ in range(27)]

    for i in range(len(data)):
        if data[i] != data[i-1] and al[ord(data[i])-97] >= 1:
            break
        else:
            al[ord(data[i]) - 97] += 1

    if sum(al) == len(data):
        count += 1

print(count)