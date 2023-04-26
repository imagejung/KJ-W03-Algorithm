# 최소 스패닝 트리(Kruskal)

# 입력부
import sys
v,e = map(int, sys.stdin.readline().split())

# 간선 e를 저장하는 list
e_list = []
for i in range(e):
    e_list.append(list(map(int, sys.stdin.readline().split())))
# 간선의 가중치를 기준으로 오름차순 정렬
e_list.sort(key = lambda x:x[2])

# 루트를 저장하는 v_root 배열
# 유니온 파인드 : 처음에는 자기 자신을 저장. 이후에는 가장 작은 값을 대표 부모노드로 바꿔줌
v_root = [i for i in range(v+1)]

def find_root(x):
    if x != v_root[x]:
        v_root[x] = find_root(v_root[x])
    return v_root[x]

#union
ans = 0
for s,e,w in e_list:
    # 가중치가 가장 낮은 간선부터 선택하여 루트 찾음
    s_root = find_root(s)
    e_root = find_root(e)
    # 루트가 달라야만 최소스패닝트리를 구성하기 위한 간선 선택할 수 있음.
    # 루트가 다르면, union해주고 (값이 가장 작은 노드(대표 부모노드)로 루트값을 바꿔주고)
    # 가중치를 답에 더해줌 (최소 스패닝 트리 구성할 간선이므로)
    if s_root != e_root:
        if s_root > e_root:
            v_root[s_root] = e_root
        else:
            v_root[e_root] = s_root
        # 루트가 다르므로 간선 선택할 수 있음. 답에 가중치 더해줌
        ans += w

print(ans)
