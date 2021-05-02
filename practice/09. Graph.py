
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

'''
6 4
1 4
2 3
2 4
5 6
'''

# 특정 원소가 속한 집합을 찾기
# def find_parent(parent, x):
#     # 루트노드가 아니라면, 루트 노드를 찾을 때까지 재귀적 호출
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     else:
#         return x

# 경로 압축기법 코드
# 기존 시간복잡도는 O(V) 
# 개선된 알고리즘을 사용하면 시간복잡도는 O(V+M(1+logV))정도로 줄어듬
def find_parent(parent, x):
    if parent[x] != x:
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

if __name__ == "__main__":
    disjoint_sets()