data = []
for i in range(5):
    data.append(int(input()))
if data[-1] - data[2] >= 0:
    print(min(data[0]*data[-1],data[1]+(data[-1]-data[2])*data[3]))
else:
    print(min(data[0]*data[-1],data[1]))