#특정 거리의 도시 찾기

import sys
from collections import deque

#입력부 (배열 0자리 무시, 도시 번호와 배열 자리 맞추기 위해)
n, m, k, x = map(int, (sys.stdin.readline().split()))
graph = [[] for i in range(n+1)]

#간선 저장
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

#거리정보 저장, 한 번도 안간 도시는 -1로 채워놓음
distance = [-1] * (n+1)
distance[x] = 0


#bfs
q = deque([x])
while q:
    loc = q.popleft()

    #아래 for i도시가 한번도 안간 도시이면(값이 -1) +1해서 이동하면 최소거리.
    #distance[i]에 loc+1 저장해주기
    for i in graph[loc]:
        if distance[i] == -1:
            distance[i] = distance[loc] + 1
            #i도시 에서 갈 수 있는 도시 추가 탐색 필요하므로 deque에 저장하여 또 탐색
            q.append(i)

if k in distance:
    for i in range(1, n+1):
        if distance[i] == k:
            print(i)
else:
    print(-1)