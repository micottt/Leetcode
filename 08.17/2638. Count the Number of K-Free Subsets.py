"""
You are given an integer array nums, which contains distinct elements and an integer k.

A subset is called a k-Free subset if it contains no two elements with an absolute difference equal to k. Notice that
the empty set is a k-Free subset.

Return the number of k-Free subsets of nums.

A subset of an array is a selection of elements (possibly none) of the array.
"""

from collections import defaultdict


class Solution:
    def countTheNumOfKFreeSubsets(self, nums: list[int], k: int) -> int:

        dic = set(nums)
        seen = set()

        k_list = defaultdict(list)
        nums.sort()
        for num in nums:

            if num - k in seen:
                continue

            k_list[num].append(num)
            seen.add(num)
            x = num
            while num + k in dic:
                k_list[x].append(num + k)
                seen.add(num + k)
                num += k

        # print(seen)
        # print(k_list)

        ans = 1
        for l in k_list:
            li = k_list[l]
            m = len(li)
            dp = [2] * m
            if m >= 2:
                dp[1] = 3
                for i in range(2, m):
                    dp[i] = dp[i - 1] + dp[i - 2]

                # print(dp)
            ans *= dp[-1]

        return ans


nums = [2, 3, 5, 8]
k = 5
x = Solution()
x.countTheNumOfKFreeSubsets(nums, k)