__author__ = 'nvishwakarma'
#For teaching purposes
#sequence/iterable can be unpacked

import math as m

p = (4, 5)
x, y = p
print("X:"+str(x),"\n", "Y:"+str(y))

list1 = ["Woody", "32", "1", (2011, 12, 21)]
Name, Age, ToyNumber, date = list1
#print("Name:"+Name, "Age:"+Age, "Serial#:"+ToyNumber, "Date:"+str(date[0])+'-'+str(date[1])+'-'+str(date[2]))
#print("Name:",Name, "Age:", Age, "Serial#:", ToyNumber, "Date:", date[0],date[1],date[2])
print("Name:",Name, "Age:", Age, "Serial#:", ToyNumber, "Date:", date)


#Unpacking N-elements large values

def drop_first_last(*grades):
    first, *middle, last =grades
    return m.fsum(middle)/len(middle)


x = drop_first_last(1, 2, 3, 4, 5, 6, 4)
print("Average :", x)


def sales_curr_prev(*records):
    *prev, curr = records
    prev_avg = sum(prev)/len(prev)
    return prev_avg, curr


prev, curr = sales_curr_prev(10, 20, 30, 10, 50, 40, 50, 200)
if prev < curr:
    print("WooHoo!!!")
else:
    print("Nooooooo Bad Quarter!!!")


#iteration over sequence of tuples of varying length
records = [
            ('foo', 1, 2)
            ,('bar', 'hello')
            ,('foo', 3, 4)
          ]


def do_foo(x, y):
    print("foo is", x, y)

def do_bar(x):
    print("Bar is", x)

for tag, *num in records:
    if tag == 'foo':
        do_foo(*num)
    elif tag =='bar':
        do_bar(*num)

#unpack string

def str_line(line, char):
    first_field, *mid_field, last_field = line.split(char)
    print("First Field ::", first_field, "Mid Field::", mid_field, "Last Field::", last_field)

str_line("hsgdf*jskgfjg*jksdjk*jksfjk*jsdgfjk*", "*")


items = [1, 2, 3, 4, 5, 6]


def recurse_sum(items):
    head, *tail = items
    print(head, tail)
    return recurse_sum(tail) if tail else head

x = recurse_sum(items)
print("Recurs Sum is", x)