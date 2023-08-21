"""
Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the
right of nums[i].
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
    def countSmaller(self, nums: list[int]) -> list[int]:

        n = len(nums)
        after = [0] * n

        dup = [x for x in nums]
        rank = {}
        dup.sort()
        r = 1
        for num in dup:
            if num not in rank:
                rank[num] = r
                r += 1

        bit = BIT(n + 1)
        after = [0] * n
        for i in range(n - 1, -1, -1):
            num = nums[i]
            bit.update(rank[num])
            after[i] = bit.query(rank[num] - 1)

        return after


nums = [-1]
x = Solution()
print(x.countSmaller(nums))
