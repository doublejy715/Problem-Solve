import sys

data = input()
for index in range(len(data)//2):
    if data[index] != data[len(data)-index-1]:
        print(0)
        sys.exit()
print(1)
