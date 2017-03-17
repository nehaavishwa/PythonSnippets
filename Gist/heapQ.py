import heapq

nums = [1, 2, 4, 5, 6, 3, 8, 9, 23]
l = heapq.nlargest(5, nums)
print(l)
s = heapq.nsmallest(5, nums)
print(s)

portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheap)
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['shares'])
print(expensive)

x = []
pop1 = heapq.heappush(x, '10')
print(pop1)
