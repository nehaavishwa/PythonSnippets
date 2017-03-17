
nElementTuple = (1, 2, 3, 4, 5, 6, 7, 8)

k, *l, m = nElementTuple
print(k, l, m, type(l))

records = [
('foo', 1, 2),
('bar', 'hello'),
('foo', 3, 4),
]


def do_foo(*a):
    #print(a)
    #print(*a)
    for i in a:
        print('foo', i)

for i, *args in records:
    #print(i, args)
    if i == 'foo':
        do_foo(*args)


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *args, last = line.split(':')
print(uname, *args, last)