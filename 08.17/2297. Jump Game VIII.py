"""
You are given a 0-indexed integer array nums of length n. You are initially standing at index 0. You can jump from index i to index j where i < j if:

nums[i] <= nums[j] and nums[k] < nums[i] for all indexes k in the range i < k < j, or nums[i] > nums[j] and nums[k] >= nums[i] for all indexes k in the range i < k < j. You are also given an integer array costs of length n where costs[i] denotes the cost of jumping to index i.

Return the minimum cost to jump to the index n - 1.
"""

from collections import defaultdict


# class Solution:
#     def minCost(self, nums: list[int], costs: list[int]) -> int:
#
#         n = len(nums)
#
#         dic = defaultdict(set)
#
#         for i in range(n - 1):
#             dic[i].add(i + 1)
#
#             if nums[i + 1] >= nums[i]:
#                 k = i + 1
#                 while k < n - 1 and nums[k] >= nums[i]:
#                     k += 1
#                 if nums[k] < nums[i]:
#                     dic[i].add(k)
#
#             else:
#                 k = i + 1
#                 while k < n - 1 and nums[k] < nums[i]:
#                     k += 1
#                 if nums[k] >= nums[i]:
#                     dic[i].add(k)
#
#         dp = [0] * n
#
#         for i in range(n - 2, -1, -1):
#             dp[i] = min(costs[step] + dp[step] for step in dic[i])
#
#         print(dic)
#         print(dp)
#         return dp[0]

from collections import defaultdict


class Solution:
    def minCost(self, nums: list[int], costs: list[int]) -> int:
        n = len(nums)

        possible = defaultdict(set)
        maxstack = []
        minstack = []

        for j in range(n):

            while maxstack and nums[j] >= nums[maxstack[-1]]:
                possible[maxstack.pop()].add(j)

            while minstack and nums[j] < nums[minstack[-1]]:
                possible[minstack.pop()].add(j)

            maxstack.append(j)
            minstack.append(j)

        dp = [0] * n

        for i in range(n - 2, -1, -1):
            dp[i] = min(costs[step] + dp[step] for step in possible[i])

        return dp[0]


nums = [3, 2, 4, 4, 1]
costs = [3, 7, 6, 4, 2]
x = Solution()
print(x.minCost(nums, costs))
