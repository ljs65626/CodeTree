n, m = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(m)]
ans=0
visited = [False] * (n+1)
visited[1]=[True]
# Please write your code here.
# graph = [[] for _ in range(n+1)]
# for a, b in edge:
#     graph[a].append(b)
#     graph[b].append(a)

# # print(graph)

# def dfs1(vertex):
#     global ans
#     for curr_v in graph[vertex]:
#         if not visited[curr_v]:
#             visited[curr_v]=True
#             ans+=1
#             dfs1(curr_v)

# dfs1(1)
# print(ans)


graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for a, b in edge:
    graph[a][b]=1
    graph[b][a]=1
# print(graph)
def dfs2(vertex):
    global ans
    for curr_v in range(1, n+1):
        if not visited[curr_v] and graph[vertex][curr_v]==1:
            visited[curr_v]=1
            ans+=1
            dfs2(curr_v)
dfs2(1)
print(ans)

