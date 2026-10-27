from collections import deque


# 994. Rotting Oranges (썩은 오렌지)
# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:
#
# Input: grid = [[0,2]]
# Output: 0
class Solution:
    def orangeRotting(self, grid: list[list[int]]) -> int:

        m, n = len(grid), len(grid[0])
        queue = deque()  # 썩은 오렌지의 좌표 (r, c)들을 담을 BFS 큐
        fresh_count = 0  # 아직 안 썩은 오렌지의 총개수

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    # 신선한 오렌지(1)의 개수도 함께 셉니다.
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 위 아래 왼쪽 오른쪽

        # BFS 탐색 : 1분단위로 큐에 있는 오렌지들을 번지게 함.
        while queue and fresh_count > 0:
            minutes += 1

            # 현재 1분 동안 번질 수 있는 기존 썩은 오렌지 수만큼만 꺼낸다.
            for _ in range(len(queue)):
                # 이번 분에 영향력을 행사할 수 있는 오렌지들만 딱 끊어서 처리
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # 상하좌우를 확인해 신선한 오렌지(1)를 만나면
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # 썩게 만듬
                        fresh_count -= 1  # 남은 신선한 오렌지 카운트를 줄임
                        queue.append((nr, nc))  # 오렌지는 다음 1분에 또 주변을 썩게 할 테니 큐에 넣음

        return minutes if fresh_count == 0 else -1


if __name__ == "__main__":
    sol = Solution()

    # 테스트 케이스 1 (기대 출력: 1)
    grid1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print("Example 1 : ", sol.orangeRotting(grid1))

    # 테스트 케이스 2 (기대 출력: 3)
    grid2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print("Example 2 : ", sol.orangeRotting(grid2))
