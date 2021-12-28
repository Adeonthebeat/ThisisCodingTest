import sys
# 재귀함수와 스택

def dfs(x):
    if x > 0:
        dfs(x-1)
        # 스택의 중요성.
        # 스택자료 구조는 복귀주소를 저장
        print(x, end=' ')

if __name__=="__main__":
    dfs(3)