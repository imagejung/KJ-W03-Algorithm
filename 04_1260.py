#DFS와 BFS

import sys
from collections import deque

#n:노드 개수, m:간선 개수, v:시작 노드 번호
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

#graph 오름차순으로 정렬
for i in range(n+1):
    graph[i].sort()

def dfs(x):
    visited[x] = 1
    print(x, end=' ')
    for i in graph[x]:
        if visited[i] == 0:
            dfs(i)

def bfs():
    print(v, end=' ')
    visited[v] = 1
    while q:
        x = q.popleft()
        for i in x:
            if visited[i] == 0:
                print(i, end=' ')
                visited[i] = 1
                q.append(graph[i])


#dfs
visited = [0 for i in range(n + 1)]
dfs(v)
print()

#bfs
q = deque([])
q.append(graph[v])
visited = [0 for i in range(n + 1)]
bfs()