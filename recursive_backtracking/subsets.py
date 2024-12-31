# # 78. Subsets
# # Medium
# # Topics
# # Companies
# # Given an integer array nums of unique elements, return all possible
# # subsets
# # (the power set).

# # The solution set must not contain duplicate subsets. Return the solution in any order.


# # Example 1:

# # Input: nums = [1, 2, 3]
# # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# # Example 2:

# # Input: nums = [0]
# # Output: [[], [0]]


# # Constraints:

# # 1 <= nums.length <= 10
# # -10 <= nums[i] <= 10
# # All the numbers of nums are unique.
# 78. Subsets
# Medium
# Topics
# Companies
# Given an integer array nums of unique elements, return all possible
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]


# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res, sol = [], []

        def backtrack(start):
            if start == n:
                res.append(sol[:])
                return

            # dont pick nums[start] -> left path
            backtrack(start + 1)

            # pick nums[start] -> right path
            # three steps: add, backtrack, remove
            sol.append(nums[start])
            backtrack(start + 1)
            sol.pop()

        backtrack(0)
        return res


# Time: O(2^n)
# Space: O(n)

# test cases
nums = [1, 2, 3]
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
print(Solution().subsets(nums))

