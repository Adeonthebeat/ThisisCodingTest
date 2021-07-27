'''
# 그래프 이론 문제
- 서로소 집합
  : 서로소 집합은 공통 원소가 없는 두 집합. 이 때 집합 간의 관계를 파악하기 위해
  서로소 집합 알고리즘을 사용할 수 있는데 서로소 집합 알고리즘은 union-find(합치기 찾기) 연산으로
  구성되며 모든 노드는 자신이 속한 집합을 찾을 때 루트 노드를 재귀적으로 찾음
  서로소 집합 알고리즘은 최소 신장 트리를 찾는 크루스칼 알고리즘에서 사용되기도 하므로 중요함

- 신장 트리
  : 신장 트리는 하나의 그래프가 있을 때, 모든 노드를 포함하는 부분 그래프를 의미
  신장 트리 구성문제는 '모든 ㅅ검을 도로를 이용해 연결하는 문제'에서 사용할 수 있음

- 크루스칼 알고리즘
  : 크루스칼 알고리즘은 가능한 최소 비용의 신장 트리를 찾아주는 알고리즘
  시간복잡도는 O(ElogE)로 간선을 정렬한 뒤에 간선의 비용이 작은 순서대로 차례대로
  최소 신장 트리를 만들어가는 그리디 알고리즘의 일종

- 위상정렬 알고리즘
  : 위상 정렬 알고리즘은 방향 그래프의 모든 노드들을 방향성에 거스르지 않도록
  순서대로 나열하는 정렬 기법을 의미함. 예시로는 '선수과목을 고려한 학습순서 설정문제'
  큐 자료구조를 이용한 위상 정렬의 시간 복잡도는 O( E + V )

  서로소 집합 문제와 최소 신장 트리 알고리즘은 코딩 테스트의 문제로 출제되며,
  위상 정렬 알고리즘은 난이도가 높은 후반부 문제에서 주로 출제 됨

'''

'''
# 여행계획 문제
 - N개의 도시
 - M개의 여행 계획에 속한 도시의 수
 - N X N 행렬 : 두 여행지의 여부 -> 1(연결) || 0(비연결)
 - 마지막줄 : `여행 계획에 포함된 모든 여행지의 번호
 - 여행 계획이 가능한지 여부를 출력하시오.
 
# Developer`s Kick!
 - '여행계획'에 해당하는 모든 노드가 같은 집합에 속하기만 하면 가능한 여행경로
 - 서로소 집합 자료구조를 이용한 문제

Input01
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
 
Output01
YES

'''


def travel_plan():
    # 여행지의 개수와 여행 계획에 속한 여행지의 개수
    n, m = map(int, input().split())

    # 부모 테이블 초기화
    parent = [0] * (n + 1)

    # 부모 테이블 상에서 부모를 자기 자신으로 초기화
    for i in range(1, n + 1):
        parent[i] = i

    # union 연산을 각각 수행
    for i in range(n):
        data = list(map(int, input().split()))
        for j in range(n):
            # 연걸된 경우(1), union 연산 수행
            if data[j] == 1:
                union_parent(parent, i + 1, j + 1)

    # 여행 계획 입력하기
    plan = list(map(int, input().split()))

    ret = True
    # 여행 계획에 속하는 모든 노드의 루트가 동일한지 확인
    for i in range(m - 1):
        if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
            ret = False

    # 여행 계획에 속하는 모든 노드가 서로 연결되어 있는지(루트가 동일한지) 확인
    if ret:
        print('YES')
    else:
        print('NO')


# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드르르 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
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
# 탑승구 문제
 - 1 ~ G개의 탑승구
 - P개의 비행기 => i번째 비행기를 1번부터 g번째 탑승구 중 하나에 영구적으로 도킹
 - 다른 비행기가 도킹하지 않은 탑승구에만 도킹 가능
 - 탑승구에 도킹할 수 없는 비행기가 나오는 경우, 그 시점부터 공항의 운행을 중지
 - 비행기를 최대 몇 대 도킹할 수 있는지 출력하는 프로그램을 작성하시오. 
# Developer`s Kick!
 - 모든 루트 노드는 자기 자신을 가리킴
 - 가능한 큰 번호 탑승구로 도킹 시도
 - 도킹하는 과정의 합집합 연산 -> 해당 집합의 왼쪽 집합과 합집합 연산
 - 루트가 0이면, 더 이상 도킹이 불가능한 것
 
Input01
4
3
4
1
1

Output01
2

'''


def docking():
    # 탑승구의 개수 입력받기
    g = int(input())

    # 비행기의 개수 입력받기
    p = int(input())

    # 부모 테이블 초기화
    parent = [0] * (g + 1)

    # 부모 테이블 상에서 부모를 자기 자신으로 초기화
    for i in range(1, g + 1):
        parent[i] = i

    ret = 0
    for _ in range(p):
        # 현재 비행기의 탑승구의 루트 확인
        data = find_parent(parent, int(input()))
        # 현재 루트가 0이라면, 종료
        if data == 0:
            break
        # 그렇지 않다면, 바로 왼쪽의 집합과 합치기
        union_parent(parent, data, data - 1)
        ret += 1
    print(ret)


'''
# 어두운 길 문제
 - N개의 집(0 ~ N-1)과 M개의 도로로 구성
 - 가로등의 비용은 도로의 길이와 비례 ( 도로길이 7 -> 7의 비용)
 - x,y,z = x번 집, y번 집사이의 도로가 있으며, z의 길이를 지님 
 - 가로등을 비활성화하여 최대로 절약하고자 함
 - 마을의 집과 도로의 정보가 주어졌을 때, 일부 가로등을 비활성화하여 절약할 수 있는 최대금액을 출력하시오.
# Developer`s Kick!
 - 최소한의 비용으로 모든 집을 연결
 - 최소 신장 트리
 - '임의의 두 집에 대하여 가로등이 켜진 도로만으로 오갈 수 있도록' - 최소신장트리
 - 그래프를 구성한 뒤, 크루스칼 알고리즘 수행
 - 절약할 수 있는 최대 금액 = 전체 가로등을 켜는 비용 - 최소 신장 트리를 구성하는 비용
 
Input01
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11

Output01
51

'''


def dark_road():
    # 노드의 개수, 간선의 개수
    n, m = map(int, input().split())

    # 부모 테이블 초기화
    parent = [0] * (n + 1)

    # 모든 간선을 담을 리스트와 최종 비용을 담을 변수
    edges = []
    ret = 0

    # 부모 테이블상에서 부모를 자기 자신으로 초기화
    for i in range(1, n + 1):
        parent[i] = i

    # 모든 간선에 대한 정보 입력 받기
    for _ in range(m):
        x, y, z = map(int, input().split())
        # 비용순으로 정렬하기 위한 튜블의 첫 번째 원소를 비용으로 설정
        edges.append((z, x, y))

    # 간선을 비용순으로 출력
    edges.sort()
    tot = 0

    # 간선을 하나씩 확인
    for edge in edges:
        cost, a, b = edge
        tot += cost
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            ret += cost

    print(tot - ret)

'''
# 행성 터널 문제
 - 행성은 3차원의 좌표 한점
 - 두 행성 A(x, y, z), B(x, y, z)을 연결하는 터널을 만드는 비용 min(|xa - xb|,|ya - yb|,|za - zb|)
 - 터널은 N-1개를 건설해서 모든 행성을 연결하는 최소비용을 구하시오. 
# Developer`s Kick!
 - '터널은 N-1개를 건설' = 최소신장트리
 - 터널 비용 min(|xa - xb|,|ya - yb|,|za - zb|)이 주어졌을 때, 
   x만 고려하자면, (11, -15, -15), (14, -5, -15), (-1, -1, -5), (10, -4, -1), (19, -4, 19)
   x는 -1, 10, 11, 14, 19 => 11, 1, 3, 5
   즉, y, z축을 무시하고 x축에 대해서는 4개의 간선만 사용해서 최소신장트리를 만들 수 있음
   결과적으로 x, y, z축에 대해여 정렬이후에 각각 N-1개의 간선만 고려해도 답이 나옴 
   문제풀이를 위한 총 간선 개수는 3 X (N-1)이며, 이를 이용해 크루스칼 알고리즘을 수행하면 제한시간에 해결가능  
 
Input01
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19

Output01 
4

'''

def turnel():

    # 노드의 개수 입력 받기
    n = int(input())

    # 부모 테이블 초기화
    parent = [0] * (n + 1)

    # 모든 간선을 담을 리스트와 최종 비용 변수
    edges = []
    ret = 0

    # 부모 테이블에서 부모를 자기 자신으로 초기화
    for i in range(1, n+1):
        parent[i] = i

    x = []
    y = []
    z = []

    # 모든 노드에 관한 좌표 값 입력 받기
    for i in range(1, n + 1):
        data = list(map(int, input().split()))
        x.append((data[0], i))
        y.append((data[1], i))
        z.append((data[2], i))

    x.sort()
    y.sort()
    z.sort()

    # 인접한 노드로부터 간선정보를 추출하여 처리
    for i in range(n - 1):
        # 비용 순으로 정렬하기 위해서 첫 번째 원소를 비용으로 설정
        edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
        edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
        edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

    # 간선을 비용 순으로 정렬
    edges.sort()

    # 간선을 하나씩 확인
    for edge in edges:
        cost, a, b = edge

        # 사이클이 발생하지 않는 경우에만, 집합 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            ret += cost

    print(ret)




if __name__ == "__main__":
    # travel_plan()
    # docking()
    # dark_road()
    turnel()
