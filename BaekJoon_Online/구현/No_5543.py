bugr = []
juice = []
for _ in range(3):
    bugr.append(int(input()))
for i in range(2):
    juice.append(int(input()))
print(min(bugr)+min(juice)-50)