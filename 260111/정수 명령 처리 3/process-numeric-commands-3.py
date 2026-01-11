from collections import deque

n=int(input())

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

for _ in range(n):
    ins = input()
    if ins.startswith('push_front'):
        _, v = ins.split()
        v = int(v)
        dq.push_front(v)
    elif ins.startswith('push_back'):
        _, v = ins.split()
        v = int(v)
        dq.push_back(v)
    elif ins == 'pop_front':
        print(dq.pop_front())
    elif ins == 'pop_back':
        print(dq.pop_back())
    elif ins=='size':
        print(dq.size())
    elif ins=='empty':
        if dq.empty():
            print(1)
        else:
            print(0)
    elif ins=='front':
        print(dq.front())
    else:
        print(dq.back())