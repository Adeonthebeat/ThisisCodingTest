

# 347. Top K Frequent Elements(상위 K개 빈출 요소)
# 정렬 (Bucket Sort): 빈도수를 인덱스로 활용하여 $O(n)$ 선형 시간에 해결 (가장 추천)

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
# Example 3:
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# Output: [1,2]

from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        # 각 빈도수 계산
        # 예 Counter([1,1,1,2,2,3]) -> {1:3, 2:2, 3:1}
        count = Counter(nums)

        # 빈도수를 인덱스로 사용하는 버킷 생성
        # 등장횟수 = len(nums) + 1
        # 빈도수가 크면 클수록 뒤로 저장
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)

        # 빈도수가 높은쪽부터 순회하며 k개 수집
        result = []
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    # 기대 출력: [1, 2] (순서 무관)
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    print("Example 1 :", sol.topKFrequent(nums1, k1))

    # Example 2
    # 기대 출력: [1]
    nums2 = [1]
    k2 = 1
    print("Example 2 :", sol.topKFrequent(nums2, k2))

    # Example 3
    # 기대 출력: [1, 2] (순서 무관)
    nums3 = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
    k3 = 2
    print("Example 3 :", sol.topKFrequent(nums3, k3))