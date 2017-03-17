a = set()
def average(array):
    # your code goes here
    a = set(array)
    sum = 0
    print(a)
    for i in a:
        sum = sum+i
    return sum/len(a)

x = average([161, 182, 161, 154, 176, 170, 167, 171 ,170, 174])
print(x)


a = input()

