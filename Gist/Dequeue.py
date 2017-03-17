from collections import deque

# keeping last N-items
q = deque(maxlen=5)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
print(q)
q.append(6)
print(q)
q.pop()
print(q)
q.popleft()
print(q)

#Complexity O(1), unlike list where complexity is O(N)
