from collections import deque
N = int(input())
visited = [0] * 1_000_001
score = [0] * 1_000_001
q = deque()
# Please write your code here.


def push(n, v):
    visited[n]=True
    score[n] = v
    q.append(n)


def bfs():
    while q:
        curr_node = q.popleft()
        for process in range(4):
            if process==0:
                if curr_node<1_000_000:
                    next_node = curr_node+1
                    if visited[next_node]==False:
                        push(next_node, score[curr_node]+1)
            elif process==1:
                if curr_node>0:
                    next_node = curr_node-1
                    if visited[next_node]==False:
                        push(next_node, score[curr_node]+1)
            elif process==2:
                if curr_node%2==0:
                    next_node = curr_node//2
                    if visited[next_node]==False:
                        push(next_node, score[curr_node]+1)
            else:
                if curr_node%3==0:
                    next_node = curr_node//3
                    if visited[next_node]==False:
                        push(next_node, score[curr_node]+1)

push(N, 0)
bfs()

if visited[1]==True:
    print(score[1])
