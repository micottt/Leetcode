"""
You are given a 2D array of strings equations and an array of real numbers values, where equations[i] = [Ai, Bi] and
values[i] means that Ai / Bi = values[i].

Determine if there exists a contradiction in the equations. Return true if there is a contradiction, or false otherwise.

Note:

When checking if two numbers are equal, check that their absolute difference is less than 10-5. The testcases are
generated such that there are no cases targeting precision, i.e. using double is enough to solve the problem.
"""


class Solution:
    def checkContradictions(self, equations: list[list[str]], values: list[float]) -> bool:

        dic = {}

        def get(x):

            if x not in dic:
                dic[x] = (x, 1)

            x_group, x_weight = dic[x]

            if x_group != x:
                new_group, new_weight = get(x_group)
                dic[x] = (new_group, x_weight * new_weight)

            return dic[x]

        def union(x, y, val):

            x_id, x_weight = get(x)
            y_id, y_weight = get(y)

            if x_id != y_id:
                dic[x_id] = (y_id, y_weight * val / x_weight)

        for (x, y), val in zip(equations, values):
            union(x, y, val)

        # print(dic)
        for (x, y), val in zip(equations, values):
            x_id, x_weight = get(x)
            y_id, y_weight = get(y)

            if abs(x_weight / y_weight - val) > 10 ** -5:
                # print(x_weight, y_weight, val)
                return True

        return False


equations = [["qzdaa", "qzdaa"], ["a", "txa"], ["qzdaa", "qzdaa"], ["qzdaa", "qzdaa"], ["qzdaa", "a"]]
values = [1, 5.36, 1, 1, 3.73]
x = Solution()
x.checkContradictions(equations, values)
