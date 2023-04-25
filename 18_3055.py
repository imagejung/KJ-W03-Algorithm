#탈출

import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
graph = []
q = deque()
#입력받으면서, 물(*) 위치는 w로 q에 넣어주고, 고슴도치(S) 위치는 s에 저장
for i in range(r):
    tmp = list(sys.stdin.readline().rstrip())
    for j in range(c):
        if tmp[j] == '*':
            q.append(['w',i,j])
        elif tmp[j] == 'S':
            s = ['s',i,j]
    graph.append(tmp)

#물 다 들어간 다음, 고슴도치 위치 q에 넣기 + time에 고슴도치 시작점 시간 0으로 넣어줌
q.append(s)
time = [[-1]*c for i in range(r)]
time[s[1]][s[2]] = 0

#BFS로 탐색
dr, dc = [1,0,-1,0], [0,1,0,-1]

while q:
    case, q_r, q_c = q.popleft()

    #물 이동
    if case == 'w':
        for i in range(4):
            a = q_r + dr[i]
            b = q_c + dc[i]
            #상하좌우 4방향에 대하여  범위안이고 and 굴X and 물X and 돌X 이면 물 늘려주기
            if 0<=a<r and 0<=b<c and graph[a][b] != 'D' and graph[a][b] != '*' and graph[a][b] != 'X':
                graph[a][b] = '*'
                q.append(['w',a,b])

    #고슴 도치 이동
    elif case == 's':
        for i in range(4):
            a = q_r + dr[i]
            b = q_c + dc[i]
            # 비버의 굴로 도착하면 시간+1 break
            if 0 <= a < r and 0 <= b < c and graph[a][b] == 'D':
                time[a][b] = time[q_r][q_c] + 1
                print(time[a][b])
                exit(0)
            # 물이 아니고, 간적이 없는 곳이면(time 값이 -1이면) 이동하여 DFS 탐색
            elif 0 <= a < r and 0 <= b < c and graph[a][b] == '.' and time[a][b] == -1:
                time[a][b] = time[q_r][q_c] + 1
                q.append(['s', a, b])

print("KAKTUS")
