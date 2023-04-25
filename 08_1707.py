#이분 그래프

import sys
sys.setrecursionlimit(10**6)
k = int(sys.stdin.readline())

# x노드에 대하여 y로 변경 및 인접한 노드 검증 (재귀로 DFS)
def dfs(x, y):
    # error가 true면 함수 끝내기 (이웃한 노드가 같은 y값)
    global error
    if error:
        return

    # x를 y로 놓고 인접한 노드 -y로 변경(재귀) 또는 -y인지 검증
    visited[x] = y
    # 인접한 노드에 대하여
    for i in graph[x]:
        # 방문한 적이 없으면 dfs함수로 변경 및 검증
        if visited[i] == 0:
            dfs(i,-y)
        # 인접한 노드가 현재 노드와 같은 y이면 이분 그래프가 아니므로 함수 종료
        elif visited[i] == y:
            error = True
            return

for i in range(k):
    # 입력부
    v,e = map(int, sys.stdin.readline().split())
    graph = [[] for i in range(v+1)]
    for j in range(e):
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    # 방문 여부 확인. 및 error false로 세팅
    visited = [0] * (v+1)
    error = False
    # 방문 안했으면 dfs로 검증
    for j in range(1,v+1):
        if visited[j] == 0:
            dfs(j,1)

    if error:
        print("NO")
    else:
        print("YES")
