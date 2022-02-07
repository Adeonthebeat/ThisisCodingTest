# 위상정렬은 어떤 일을 하는 순서를 찾는 알고리즘
# 각각의 일의 선후관계가 복잡하게 얽혀있을 때,
# 각각 일의 선후관계를 유지하면서 전체 일의 순서를 짜는 알고리즘
from collections import deque
# 6 6
# 1 4
# 5 4
# 4 3
# 2 5
# 2 3
# 6 2

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
degree = [0] * (n + 1)

Q = deque()

# 방향그래프 그려주기
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    degree[b] += 1

for i in range(1, n + 1):
    # 차수가 0인 것 -> 바로 작업해도 됨
    if degree[i] == 0:
        Q.append(i)

while Q:
    x = Q.popleft()
    print(x, end=' ')

    for i in range(1, n + 1):
        # x ->> i로 방향이 흐른다면.
        if graph[x][i] == 1:
            degree[i] -= 1 # 해당 차수를 -1 해줌
            if degree[i] == 0:
                Q.append(i)