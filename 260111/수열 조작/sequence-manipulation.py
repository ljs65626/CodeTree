from collections import deque
n = int(input())

# Please write your code here.
class Deque:
    def __init__(self):
        self.dq = deque()
    
    def push_front(self, A):
        self.dq.appendleft(A)
    
    def push_back(self, A):
        self.dq.append(A)
    
    def empty(self):
        return not self.dq
    
    def pop_front(self):
        if self.empty():
            raise Exception('Deque is Empty')
        return self.dq.popleft()
    
    def pop_back(self):
        if self.empty():
            raise Exception('Deque is Empty')
        return self.dq.pop()
    
    def size(self):
        return len(self.dq)
    
    def front(self):
        if self.empty():
            raise Exception('Deque is Empty')
        return self.dq[0]
    
    def back(self):
        if self.empty():
            raise Exception('Deque is Empty')
        return self.dq[-1]

dq = Deque()

for i in range(1, n+1):
    dq.push_back(i)

while dq.size()!=1:
    dq.pop_front()
    dq.push_back(dq.pop_front())

print(dq.front())