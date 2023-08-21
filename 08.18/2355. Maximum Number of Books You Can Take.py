"""
You are given a 0-indexed integer array books of length n where books[i] denotes the number of books on the ith shelf
of a bookshelf.

You are going to take books from a contiguous section of the bookshelf spanning from l to r where 0 <= l <= r < n.
For each index i in the range l <= i < r, you must take strictly fewer books from shelf i than shelf i + 1.

Return the maximum number of books you can take from the bookshelf.
"""


class Solution:
    def maximumBooks(self, books: list[int]) -> int:

        n = len(books)

        dp = [0] * n

        monostack = []
        track = [-1] * n
        for i in range(n - 1, -1, -1):

            while monostack and books[monostack[-1]] - (monostack[-1] - i) > books[i]:
                track[monostack.pop()] = i
            monostack.append(i)

        ans = 0
        for i in range(n):
            j = track[i]
            if j == -1:
                term = min(books[i], i + 1)
                dp[i] = max(0, (books[i] + books[i] - term + 1) * term // 2)
            else:
                dp[i] = dp[j] + (books[i] + books[i] - (i - j - 1)) * (i - j) // 2

            ans = max(ans, dp[i])

        # print(dp)
        # print(track)
        return ans


shelf = [[8, 5, 2, 7, 9], [7, 0, 3, 4, 5], [8, 2, 3, 7, 3, 4, 0, 1, 4, 3], [5, 5, 5], [0, 3, 1, 5, 4]]
x = Solution()
for books in shelf:
    print(x.maximumBooks(books))
