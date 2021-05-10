
# 그래프(Graph)란? 노드와 노드 사이에 연결된 간선의 정보를 가지고 있는 자료구조.
# 서로 다른 가체(객체)가 연결되어있다면 그래프 알고리즘
# 
# 그래프 구조
# 방향성 : 방향그래프 혹은 무방향그래프
# 순환성 : 순환 및 비순환
# 루트노드 존재여부 : 루트노드 없음 
# 노드간 관계성 : 부모와 자식관계 없음
# 모델의 종류 : 네트워크 모델

# 트리구조
# 방향성 : 방향그래프 
# 순환성 : 비순환
# 루트노드 존재여부 : 루트노드 존재 
# 노드간 관계성 : 부모와 자식관계 
# 모델의 종류 : 계층 모델

## 그래프 구현방법
# 1) 인접행렬
# 메모리 공간 : O(V^2)
# 간선 비용 : O(1)
# 알고리즘 : 플로이드워셜 알고리즘
# 노드의 개수 : V^2개

# 2) 인접리스트
# 메모리 공간 : O(E)
# 간선 비용 : O(V)
# 알고리즘 : 다익스트라(HEAP)
# 노드의 개수 : V개

# 서로소 집합 : 공통 원소가 없는 두 집합을 의미
# 집합 {1, 2}와 {3, 4}는 서로소 관계
# 서로소 집합 자료구조는 union-find(합치기 - 찾기) 자료구조

# 서로소 집합을 이용한 사이클 판별
# 서로소 집합은 무방향 그래프 내에서의 사이클 내에서의 사이클을 판별할 때 사용
# 그래프의 사이클 여부는 DFS(Deep First Search)을 통해 판별

# 사이클 알고리즘
# 1. 각 간선을 확인하며 두 노드의 루트노드를 확인
#  루트노드가 서로 다르다면, 두 노드에 대해 UNION 연산을 수행
#  루트노드가 서로 같다면, 사이클(Cycle)이 발생할 것
# 2. 그래프에 포함되어있는 모든 간선에 대해 1번과정을 반복

# 신장트리(Spanning Tree)
# : 하나의 그래프가 있을 때, 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미
# 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는 조건이 트리의 성립조건
# 트리 자료구조는 노드가 N일 때, 항상 간선의 개수는 N-1개이다.

# Kruskal_Algorithm(크루스칼 알고리즘) : 최소신장트리 알고리즘
# 가능한 한 최소한의 비용으로 신장 트리를 찾는 알고리즘
# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬
# 2. 간선을 하나씩 확인하며, 현재의 간선이 사이클을 발행시키는지 확인
#   사이클이 발생하지 않는 경우, 최소 신장 트리에 포함
#   사이클이 발생하는 경우, 최소 신장 트리에 포함시키지 않음
# 3. 모든 간선에 따라 2번의 과정을 반복

# 시간 복잡도 : 간선의 개수(E)일 때, O(ElogE)
# 서로소 집합 알고리즘 시간복잡도 < 정렬 시간복잡도

# 위상정렬(Topology Algorithm)
# 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때, 사용할 수 있는 알고리즘
# 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
# 1. 진입차수가 0인 노드를 큐에 넣는다.
# 2. 큐가 빌 때까지 다음의 과정을 반복한다.
# 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
# 새로게 진입차수가 0이 된 노드를 큐에 넣는다.
# 모든 원소를 방문하기 전, 큐가 비어있다면 사이클이 존재하는 것
# 큐에서 원소가 V번 추출되기 전에 큐가 비어버리면 사이클이 발생한 것.
# 시간복잡도: O(V + E)
# 모든 노드를 확인하면서 해당 노드에서 출발하는 간선을 차례대로 제거
# 위상정렬은 DAG(direct_acyclic_graph): 순환하지 않는 방향그래프의 특징
# 정답이 1가지 이상인 경우도 있다. 위상정렬을 구현할때 stack을 이용한 DFS로도 구현할 수 있다.



# 특정 원소가 속한 집합을 찾기
import copy
import sys
from collections import deque

'''
def find_parent(parent, x):
    # 루트노드가 아니라면, 루트 노드를 찾을 때까지 재귀적 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    else:
        return x
'''
# 경로 압축기법 코드(특정 원소가 속한 집합을 찾기)
# 기존 시간복잡도는 O(V) 
# 개선된 알고리즘을 사용하면 시간복잡도는 O(V+M(1+logV))정도로 줄어듬
def find_parent(parent, x):
    if parent[x] != x:
        # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

'''
6 4
1 4
2 3
2 4
5 6
'''
# 서로소 집합
def disjoint_sets():
    # 노드 개수, 간선(Union 연산)의 개수 세팅
    v, e = map(int, input().split())
    
    # 부모 테이블 초기화
    parent = [0] * (v+1)
    
    # 부모테이블 상에서 부모는 부모 자신으로 초기화 
    for i in range(1, v+1):
        parent[i] = i

    # Union 연산을 각각 수행
    for i in range(e):
        a, b = map(int, input().split())
        union_parent(parent, a, b)

    # 각 원소가 속한 집합 출력하기
    print("각 원소가 속한 집합 : ", end=' ')
    for i in range(1, v+1):
        print(find_parent(parent, i), end=' ')


    print()

    # 부모 테이블 내용 출력하기
    print("부모 테이블 : ", end=' ')
    for i in range(1, v+1):
        print(parent[i], end=' ')

def disjoint_sets_cycle():
    # 노드, 간선 개수 입력
    v, e = map(int, input().split())

    # 부모 테이블 초기화
    parent = [0] * (v+1) 
    
    # 보모 테이블상에서 부모를 자기 자신으로 초기화
    for i in range(1, v+1):
        parent[i] = i
    
    # 사이클 발생 여부
    cycle = False
    
    for i in range(e):
        a, b = map(int, input().split())
        
        # 사이클이 발생한 경우, 종료
        if find_parent(parent, a) == find_parent(parent, b):
            cycle = True
            break
        # 사이클이 발생하지 않았다면 합집합 연산 수행
        else:
            union_parent(parent, a, b)

    if cycle:
        print("사이클이 발생")
    else:
        print("사이클이 발생하지 않았습니다!")
'''
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''

# 크루스칼 알고리즘 - 최소신장 알고리즘
def Kruskal_Algorithm():
    # 노드, 간선의 개수 입력
    v, e = map(int, input().split())
    
    # 부모 테이블 초기화
    parent = [0] * (v+1)
    
    # 모든 간선을 담을 리스트와 최종 비용을 담을 변수
    edges = []
    result = 0

    # 부모테이블에서 부모 자기 자신으로 초기화
    for i in range(1, v+1):
        parent[i] = i

    # 모든 간선 정보 입력 받기
    for _ in range(e):
        a, b, cost = map(int, input().split())
        # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
        edges.append((cost, a, b))

    # 간선을 비용 순을 정렬
    edges.sort()

    for edge in edges:
        cost, a, b = edge

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    print(result)


'''
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
'''

def topology():
    # 노드, 간선 개수 입력
    v, e = map(int, input().split())

    # 모든 노드에 대한 진입 차수는 0으로 초기화
    indegree = [0] * (v+1)

    # 각 노드에 연결된 간선 정보를 담기 위한 연결리스트 초기화
    graph = [[] for i in range(v+1)]

    # 방향그래프의 모든 간선 정보 입력받기
    for _ in range(e):
        a, b = map(int, input().split())

        # 정점 A에서 B로 이동가능
        graph[a].append(b)

        # 진입차수를 1증가
        indegree[b] += 1

    def topology_sort():
        result = [] # 알고리즘 수행결과를 담을 리스트
        q = deque() # 큐 기능을 위한 deque 라이브러리

        # 처음 시작할 때, 진입차수가 0인 노드를 큐에 삽입
        for i in range(1, v+1):
            if indegree[i] == 0:
                q.append(i)

        # 큐가 빌때까지
        while q:
            # 큐에서 원소 꺼내기
            now = q.popleft()
            result.append(now)

            # 해당원소와 연결된 노드들의 진입차수에서 1빼기
            for i in graph[now]:
                indegree[i] -= 1
                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[i] == 0:
                    q.append(i)
        # 위상정렬 결과 출력
        for i in result:
            print(i, end=' ')
    topology_sort()

def find_parent_team(parent, x):
    if parent[x] != x:
        # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
        parent[x] = find_parent_team(parent, parent[x])
    return parent[x]

def union_parent_team(parent, a, b):
    a = find_parent_team(parent, a)
    b = find_parent_team(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''
# 팀 만들기 문제
def make_team():

    n, m = map(int, input().split())
    parent = [0] * (n+1) # 부모 테이블 초기화

    # 부모테이블상에서 부모를 자기 자신으로 초기화
    for i in range(0, n+1):
        parent[i] = i

    for i in range(m):
        # 팀 합치기 0 a b
        # 팀 여부   1 a b
        oper, a, b = map(int, input().split())

        # 합집합 연산인 경우
        if oper == 0:
            union_parent_team(parent, a, b)

        elif oper == 1:
            if find_parent_team(parent, a) == find_parent_team(parent, b):
                print('YES')
            else:
                print('NO')
'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''

# 커리큘럼 문제
def curriculum():
    input = sys.stdin.readline

    # 노드 개수
    v = int(input())
    
    # 모든 노드에 대한 진입차수를 0으로 초기화
    indegree = [0] * (v+1)

    # 각 노드에 연결된 간선정보를 담기위한 연결리스트 초기화
    graph = [[] for i in range(v+1)]

    # 각 강의시간을 0으로 초기화
    time = [0] * (v+1)

    # 방향 그래프의 모든 간선정보 입력받기
    for i in range(1, v+1):
        data = list(map(int, input().split()))
        time[i] = data[0]  # 시간정보
        for x in data[1:-1]:
            indegree[i] += 1
            graph[x].append(i)
        
    # 위상정렬함수
    def topology_sort():
        # 알고리즘 수행결과를 담을 리스트
        # ti
        result = copy.deepcopy(time)
        q = deque()
        
        # 처음 시작할 때 진입차수가 0인 노드를 큐에 삽입
        for i in range(1, v+1):
            if indegree[i] == 0:
                q.append(i)
        
        # 큐가 빌때까지
        while q:
            # 큐에서 원소꺼내기
            now = q.popleft()
            
            for i in graph[now]:
                result[i] = max(result[i], result[now] + time[i])
                indegree[i] -= 1
                
                # 새롭게 진입 차수가 0이되는 노드를 큐에 삽입
                if indegree[i] == 0:
                    q.append(i)

        for i in range(1, v+1):
            print(result[i])

    topology_sort()




# 특정 원소가 속한 집합 찾기
def find_parent_city(parent, x):
    if parent[x] != x:
        parent[x] = find_parent_city(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent_city(parent,a, b):

    a = find_parent_city(parent, a)
    b = find_parent_city(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 도시분할계획
# 마을을 2개로 분리하기전에 최소 신장트리(크루스칼)를 이용하면 최소값이 나온다.
# 트리 자료구조는 노드가 N개일 때 항상 간선의 개수는 N-1이다.
# 문제에서 길을 없애고 나머지 길의 유지비의 합을 최소로 하고 싶다고 적혀있는데
# 이는 가장 유지비가 많이 드는 길을 끊으면 다음 유지비가 최소가 된다는말과 동일하다.
# Developer`s Kick : 전체 그래프에서 2개의 최소 신장 트리를 만들어야 함
# 크루스칼 알고리즘으로 최소 신장 트리를 찾은 다음 최소 신장 트리를 구성하는 간선 중 가장 비용이 큰 간선을 제거하는 것

'''
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''
def city_divide():

    # 노드, 간선 개수 입력받기
    v, e = map(int, input().split())
    
    # 부모테이블 초기화
    parent = [0] * (v + 1)

    # 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
    edges = []
    result = 0  # 유지비가 최소로 드는 길 Count

    # 부모 테이블에서 부모 자기 자신 초기화
    for i in range(1, v+1):
        parent[i] = i

    # 모든 간선에 대한 정보 받기
    for _ in range(e):
        a, b, cost = map(int, input().split())
        # 비용 순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
        edges.append((cost, a, b))

    # 간선을 비용 순으로 정렬
    edges.sort()
    # 최소 신장 트리에 포함된 간선 중 가장 비용이 큰 간선
    last = 0

    # 간선을 하나씩 확인하며
    for edge in edges:
        cost, a, b = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent_city(parent, a) != find_parent_city(parent, b):
            union_parent_city(parent, a, b)
            result += cost
            last = cost

    print(result - last)

if __name__ == "__main__":
    # disjoint_sets()
    # disjoint_sets_cycle()
    # Kruskal_Algorithm()
    # topology()
    # make_team()
    # curriculum()
    city_divide()