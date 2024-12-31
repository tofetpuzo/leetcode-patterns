# 77. Combinations
# Medium
# Topics
# Companies
# Given two integers n and k, return all possible combinations of k numbers chosen from the range[1, n].

# You may return the answer in any order.


# Example 1:

# Input: n = 4, k = 2
# Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1, 2] and [2, 1] are considered to be the same combination.
# Example 2:

# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.


# Constraints:

# 1 <= n <= 20
# 1 <= k <= n
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        res, sol = [], []

        def backtrack(start):
            if len(sol) == k:
                res.append(sol[:])
                return
            for i in range(start, n + 1):
                sol.append(i)
                backtrack(i + 1)
                sol.pop()

        backtrack(1)
        return res

# Time complexity: O(N!/(N-K)!K!)
# Space complexity: O(N!/(N-K)!K!) since we have N!/(N-K)!K! combinations
# Approach: Backtracking

# The idea is to generate all the combinations of the given array.

# We can do this by using backtracking.

# We start by creating an empty list called combinations.

# We then call the backtrack function with the given array, an empty path list,
# and the combinations list.

# The backtrack function is a recursive function that takes the array,
# the path list, and the combinations list.

# If the path list has k elements, we add the current path to the combinations list and return.

# Otherwise, we iterate over the array and add the current element to the path list.

# We then call the backtrack function with the updated path list and the combinations list.


# test cases
n = 4
k = 2
# Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
print(Solution().combine(n, k))


def combine(n, k):
    res, sol = [], []

    def backtrack(start):
        if len(sol) == k:
            res.append(sol[:])
            return

        # if you want to go down this path, you need to have enough numbers left
        left = start  # if the amount of numbers left is less than the amount of numbers
        # you still need, you can't go down this path
        still_need = k - len(sol)

        if left > still_need:
            backtrack(start - 1)  # we dont need it so we can skip it

        sol.append(start)
        backtrack(start - 1)
        sol.pop()

    backtrack(n)
    return res

# Time complexity: O(N!/(N-K)!K!)
