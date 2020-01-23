def binary_search(data, search):
    medium = int(len(data) / 2)
    print(data)
    if len(data) == 1 and search == data[0]:
        return True
    if len(data) == 1 and search != data[0]:
        return False
    if len(data) == 0:
        return False

    if data[medium] == search:
        return True
    elif data[medium] > search:
        binary_search(data[:medium], search)
    else:
        binary_search(data[medium+1:], search)

import random
data_list = random.sample(range(100), 10)
data_list.sort()
print(data_list)
print(binary_search(data_list, 66))
