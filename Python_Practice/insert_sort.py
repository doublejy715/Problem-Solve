# 단순히 스왑 형식으로 마무리 할 수 있다.

def Insert_Sort(data):
    for index1 in range(len(data)-1):
        for index2 in range(index1+1,0,-1):
            if data[index2] < data[index2-1]:
                data[index2], data[index2-1] = data[index2-1],data[index2]
            else:
                break
    return data