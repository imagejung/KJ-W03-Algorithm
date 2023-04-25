# 아침 산책

import sys
sys.setrecursionlimit(10**6)

# (입력)노드 개수
n = int(sys.stdin.readline())

# (입력)실내/실외 1=실내 0=실외, inout index번호 node번호랑 동기화
inout = [0]
tmp = list(map(int, sys.stdin.readline().rstrip()))
inout.extend(tmp)

# (입력)그래프 입력
sum = 0 #답
graph = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    #실외 + 실외 인접이면, 두개 사이에 실외가 없어서 카운트가 안됨. 바로 *2 해서 더해줌
    if inout[a] == 1 and inout[b] == 1:
        sum += 2


# 실외를 기준으로, 실외에 무리에 인접한 실내 갯수를 파악(by DFS)
def dfs (start, cnt):
    visited[start] = 1
    for i in graph[start]:
        # 인접한 노드가 실내이면 cnt +1
        if inout[i] == 1:
            cnt += 1
        # 인접한 노드가 실외이면 방문체크하고 dfs 실내 추가 검토
        elif inout[i] == 0 and visited[i] == 0:
            cnt = dfs(i, cnt)
    return cnt # 인접한 실내 갯수 return


# 모든 실외 노드를 기준으로 dfs검토
visited = [0] * (n+1)
for i in range(1, n+1):
    if visited[i] == 0 and inout[i] == 0:
        x = dfs(i,0)
        sum += x * (x-1)

print(sum)