# 알파코드(DFS)
# 25114

def dfs(idx, p):
    global cnt
    if idx == n:
        cnt += 1
        for j in range(p):
            print(chr(ret[j] + 64), end='')
        print()
    else:
        for i in range(1, 27):
            if code[idx] == i:
                ret[p] = i
                dfs(idx + 1, p + 1)
            elif i >= 10 and code[idx] == i // 10 and code[idx + 1] == i % 10:
                ret[p] = i
                dfs(idx + 2, p + 1)  # 두자리 숫자.


if __name__ == "__main__":
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1)  # out of index 체크.
    ret = [0] * (n + 3)
    cnt = 0
    dfs(0, 0)
    print(cnt)
