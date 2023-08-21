"""
You are given a 0-indexed integer array nums and a positive integer k.

We call an index i k-big if the following conditions are satisfied:

There exist at least k different indices idx1 such that idx1 < i and nums[idx1] < nums[i]. There exist at least k
different indices idx2 such that idx2 > i and nums[idx2] < nums[i]. Return the number of k-big indices.
"""


class BIT:

    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, idx):
        while idx <= self.size:
            self.tree[idx] += 1
            idx += idx & -idx

    def query(self, idx):
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & -idx
        return total


class Solution:
    def kBigIndices(self, nums: list[int], k: int) -> int:

        n = len(nums)
        size = max(nums)
        left = BIT(size)
        right = BIT(size)
        before = [0] * n
        after = [0] * n

        for i, num in enumerate(nums):
            left.update(num)
            before[i] = left.query(num - 1)

        for i in range(n - 1, -1, -1):
            num = nums[i]
            right.update(num)
            after[i] = right.query(num - 1)

        ans = 0
        for j in range(n):
            if before[j] >= k and after[j] >= k:
                ans += 1

        print(before, after)
        return ans


nums = [1, 2, 6, 5, 6, 2, 3]
k = 2
x = Solution()
print(x.kBigIndices(nums, k))