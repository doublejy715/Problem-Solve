data = input()
conv1 = 0
conv0 = 0

if data[0] == 1:
    conv0 += 1
else:
    conv1 += 1

for _ in range(len(data)-1):
    # 먼저 1에서 0으로 바뀌는 경우
    if data[_] == '1' and data[_+1] == '0':
        # 0으로 모두 바꿔줘야 하는 경우
        conv0 += 1
    elif data[_] == '0' and data[_+1] == '0':
        conv1 += 1

print(min(conv0,conv1))