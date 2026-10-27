import sys

sys.setrecursionlimit(10 ** 6)


# 200. Number of islands(섬의 개수)

# '1'(육지)과 '0'(물)로 이루어진 지도 형태의 m x n 2D 이진 격자판 grid가 주어질 때, 섬의 개수를 반환하세요.

# Example 1:
# Input: grid =
# [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        if not grid:
            return 0

        m, n = len(grid), len(grid)
        island_count = 0

        def dfs(r: int, c: int):
            # r < 0 or r >= m: 행 좌표가 격자의 위/아래 경계를 벗어남
            # c < 0 or c >= n
            # grid[r][c] != '1' 물인 경우.
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
                return

            grid[r][c] = '0'  # 방문처리

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r, c)

        return island_count


if __name__ == "__main__":
    sol = Solution()

    # 테스트 케이스 1 (기대 출력: 1)
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print("Example 1:", sol.numIslands(grid1))

    # 테스트 케이스 2 (기대 출력: 3)
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print("Example 2:", sol.numIslands(grid2))