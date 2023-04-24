#토마토

#입력부
import sys
from collections import deque
m, n, h = map(int, sys.stdin.readline().split())


#토마토 내용 입력 받으면서, 익은 토마토 위치 q에 deque로 저장
q = deque([]) #익은 토마토 위치
graph = [] #전체 좌표
for k in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for i in range(m):
            if tmp[j][i] == 1:
                q.append([k,j,i]) #익은 토마토 위치 저장
    graph.append(tmp) #전체 좌표 저장

dh = [1,-1,0,0,0,0]
dn = [0,0,1,-1,0,0]
dm = [0,0,0,0,1,-1]

#BFS로 검토
while q:
    #토마토 6방향으로 검토하여 0이면(익지 않았으면) 익게 만들고, 익은 토마토 좌표 queue에 넣어서
    #다시 6방향씩 컴토. 몇일째에 익었는지 graph에 기록
    loc_h,loc_n,loc_m = q.popleft()

    #a,b,c는 검토하는 임시 변수
    for i in range(6):
        a = loc_h + dh[i]
        b = loc_n + dn[i]
        c = loc_m + dm[i]

        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c] == 0:
            q.append((a,b,c))
            graph[a][b][c] = graph[loc_h][loc_n][loc_m] + 1

#graph 안에 0 남아있으면 -> 안익은 토마토 존재 : print(-1)
#0이 없으면 최대값-1 이 모든 토마토 익는데 필요한 날
day = 0
for k in range(h):
    for j in range(n):
        for i in range(m):
            if graph[k][j][i] == 0:
                print(-1)
                exit(0)
            else:
                if graph[k][j][i] > day:
                    day = graph[k][j][i]

print(day-1)