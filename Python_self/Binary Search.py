def Binary_Search(data,search):
    if len(data) <= 1 and search == data[0]:
        return True
    elif len(data) <= 1 and search != data[0]:
        return False
    mid = int(len(data)/2)
    if data[mid] == search:
        return True
    elif data[mid] >= search:
        return Binary_Search(data[:mid],search)
    else:
        return Binary_Search(data[mid:],search)


data = [15,6,7,35,7,3,2,5,36,23,43,34,545,345,3456]
data.sort()
print(data)
print(Binary_Search(data,335))