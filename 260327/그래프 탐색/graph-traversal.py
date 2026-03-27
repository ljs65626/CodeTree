n, m = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
ans=0
visited = [False] * (n+1)
visited[1]=[True]
# Please write your code here.
for a, b in edge:
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

def dfs(vertex):
    global ans
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v]=True
            ans+=1
            dfs(curr_v)

dfs(1)
print(ans)

