from math import inf

def divide(first, second):
    if second == 0:
        return  inf
    else:
        a = first / second
        print(a)
result = divide(5  , 0)
print(result)
