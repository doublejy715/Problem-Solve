while True:
    num = int(input())
    data = []
    if num == -1:
        break
    for i in range(1,num):
        if num % i == 0:
            data.append(i)
    if sum(data) == num:
        print('{} = '.format(num),end="")
        for index in range(len(data)):
            if index == 0:
                print(data[index],end="")
            elif index == (len(data) - 1):
                print(' + {}'.format(data[index]))
            else:
                print(' + {}'.format(data[index]),end="")
    else:
        print('{} is NOT perfect.'.format(num))