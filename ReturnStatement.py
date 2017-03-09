__author__ = 'nvishwakarma'


def addition(*arg1):
    i = 0
    for i in arg1:
        i += i
    return i


#def substraction(arg1, arg2):
subs = lambda arg1, arg2: arg1 - arg2
#    return subs


a = subs(20, 10)
print(a)