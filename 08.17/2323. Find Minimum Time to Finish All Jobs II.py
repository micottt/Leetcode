"""
You are given two 0-indexed integer arrays jobs and workers of equal length, where jobs[i] is the amount of time needed to complete the ith job, and workers[j] is the amount of time the jth worker can work each day.

Each job should be assigned to exactly one worker, such that each worker completes exactly one job.

Return the minimum number of days needed to complete all the jobs after assignment.
"""

from math import ceil
import heapq

# class Solution:
#
#     def minimumTime(self, jobs: list[int], workers: list[int]) -> int:
#
#         jobs.sort()
#         workers.sort()
#
#         ans = float("-inf")
#
#         for job, worker in zip(jobs, workers):
#
#             ans = max(ans, ceil(job / worker))
#
#         return ans


class Solution:

    def minimumTime(self, jobs: list[int], workers: list[int]) -> int:
        n = len(jobs)

        heapq.heapify(jobs)
        heapq.heapify(workers)

        days = float("-inf")
        while jobs:
            job = heapq.heappop(jobs)
            worker = heapq.heappop(workers)
            # print(job, worker)

            time = ceil(job / worker)

            days = max(days, time)

        return days
