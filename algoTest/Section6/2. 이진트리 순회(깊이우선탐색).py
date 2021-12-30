# 이진트리 순회(깊이우선탐색)
# 1245367 # 전위순회 루트 - 왼 - 오
# 4251367 # 중위순회 왼 - 루트 - 오
# 4526731 # 후위순회 왼 - 오 - 루트

def dfs(x):
    if x > 7:
        return
    else:
        # print(x, end=' ')   # 전위순회
        dfs(x * 2)          # 왼쪽 노드
        # print(x, end=' ')   # 중위순회
        dfs(x * 2 + 1)      # 오른쪽 노드
        print(x, end=' ')   # 후위순회


if __name__ == "__main__":
    dfs(1)
