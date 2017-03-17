import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, items, priority):
        heapq.heappush(self._queue, (-priority, self._index, items))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

'''
class Item:
    def __init__(self, name):
        self.name =name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 2)
q.push(Item('den'), 1)
q.push(Item('loo'), 3)

print(q.pop())
'''
q = PriorityQueue()
q.push('foo', 1)
q.push('bar', 2)
q.push('den', 1)
q.push('loo', 3)

print(q.pop())
print(q.pop())
print(q.pop())

x = []
y = ()
z = {}
a = set()
print(type(x), type(y), type(z), type(a))
