from functools import cache
from collections import Counter


class Solution:
    """
    45. Jump Game II
    You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

    Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at
    nums[i], you can jump to any nums[i + j] where:

    0 <= j <= nums[i] and i + j < n Return the minimum number of jumps to reach nums[n - 1]. The test cases are
    generated such that you can reach nums[n - 1].
    """
    def jump(self, nums: list[int]) -> int:

        n = len(nums)

        dp = [0] * n
        for i in range(n - 2, -1, -1):
            if nums[i] == 0:
                dp[i] = float("inf")
                continue

            if i + nums[i] >= n - 1:
                dp[i] = 1

            else:
                dp[i] = 1 + min(dp[j] for j in range(i + 1, i + nums[i] + 1))

        print(dp)
        return dp[0]

    """
    189. Rotate Array
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
    """

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        k = k % n

        nums[:] = nums[-k:] + nums[:-k]

    """
    122. Best Time to Buy and Sell Stock II
    You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

    On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any 
    time. However, you can buy it then immediately sell it on the same day.

    Find and return the maximum profit you can achieve.
    """

    def maxProfit(self, prices: list[int]) -> int:

        n = len(prices)

        @cache
        def dp(i, hold):

            if i == n:
                return 0

            if hold:
                return max(dp(i + 1, hold), dp(i + 1, False) + prices[i])

            else:
                return max(dp(i + 1, hold), dp(i + 1, True) - prices[i])

        return dp(0, False)

    """
    151. Reverse Words in a String
    Given an input string s, reverse the order of the words.
    
    A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
    
    Return a string of the words in reverse order concatenated by a single space.
    
    Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should 
    only have a single space separating the words. Do not include any extra spaces.
    """
    def reverseWords(self, s: str) -> str:

        stack = []
        word = ""
        for ch in s:

            if ch != " ":
                word += ch

            else:
                if word:
                    stack.append(word)
                    word = ""

        if word:
            stack.append(word)
            word = ""

        return " ".join(stack[::-1])

    """
    289. Game of Life
    According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by 
    the British mathematician John Horton Conway in 1970."
    
    The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or 
    dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the 
    following four rules (taken from the above Wikipedia article):
    
    Any live cell with fewer than two live neighbors dies as if caused by under-population. Any live cell with two or 
    three live neighbors lives on to the next generation. Any live cell with more than three live neighbors dies, as 
    if by over-population. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction. 
    The next state is created by applying the above rules simultaneously to every cell in the current state, 
    where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next 
    state.
    """

    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        live = Counter()
        dead = Counter()

        directions = [(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1),(1,0),(-1,0)]

        m, n = len(board), len(board[0])

        def Valid(row, col):
            return 0 <= row < m and 0 <= col < n

        for row in range(m):
            for col in range(n):

                state = board[row][col]

                if state == 1:

                    if (row, col) not in live:
                        live[(row, col)] = 0

                    for dy, dx in directions:
                        new_row, new_col = row + dy, col + dx

                        if Valid(new_row, new_col):
                            new_state = board[new_row][new_col]

                            if new_state == 1:
                                live[(new_row, new_col)] += 1

                            else:
                                dead[(new_row, new_col)] += 1

        for cell in live:
            row, col = cell
            neighbors = live[(row, col)]
            if neighbors < 2 or neighbors > 3:
                board[row][col] = 0

        for cell in dead:
            row, col = cell
            neighbors = dead[(row, col)]
            if neighbors == 3:
                board[row][col] = 1

    """
    20. Valid Parentheses
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    
    An input string is valid if:
    
    Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order. 
    Every close bracket has a corresponding open bracket of the same type.
    """

    def isValid(self, s: str) -> bool:

        dic = {"(": ")", "[": "]", "{": "}"}

        stack = []
        for ch in s:
            if ch in dic:
                stack.append(ch)

            else:
                # print(stack)
                if not stack or dic[stack.pop()] != ch:
                    return False

        return True if not stack else False
