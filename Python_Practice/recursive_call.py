def factorial(num):
    if num <= 1:
        return num
    return num*factorial(num-1)


def multiple(num):
    if num <= 1:
        return num
    return num * multiple(num-1)


def list_sum(data):
    if len(data) <= 1:
        return data[0]
    return data[0]+list_sum(data[1:])


def palindrome(data):
    if len(data) <= 1:
        return True
    if data[0] == data[-1]:
        return palindrome(data[1:-1])
    else:
        return False


def func(n):
    print(n)
    if n == 1:
        return n
    elif n % 2 == 0 :
        return  func(int(n/2))
    else:
        return func(int(3*n+1))


for index in range(10):
    print(factorial(index))


print(multiple(10))
list1 = [1,2,3,4,5]
print(list_sum(list1))
list2 = 'leval'
print(palindrome(list2))
print(func(3))
