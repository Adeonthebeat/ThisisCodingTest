
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

'''
6 4
1 4
2 3
2 4
5 6
'''

# 특정 원소가 속한 집합을 찾기
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
        return find_parent(parent, parent[x])
    else:
        return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

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

if __name__ == "__main__":
    # disjoint_sets()
    # disjoint_sets_cycle()
    Kruskal_Algorithm()