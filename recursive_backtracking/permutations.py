# 6. Permutations
# Medium
# Topics
# Companies
# Given an array nums of distinct integers, return all the possible
# permutations
# . You can return the answer in any order.


# Example 1:

# Input: nums = [1, 2, 3]
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# Example 2:

# Input: nums = [0, 1]
# Output: [[0, 1], [1, 0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]


# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]] 
        """
        n = len(nums)
        res, sol = [], []

        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return
            for i in range(n):
                if nums[i] in sol:
                    continue
                sol.append(nums[i])
                backtrack()
                sol.pop()
        backtrack()
        return res

# Time complexity: O(N!)
# Space complexity: O(N!) since we have N! permutations

# Approach: Backtracking
# The idea is to generate all the permutations of the given array.
# We can do this by using backtracking.
# We start by creating an empty list called permutations.
# We then call the backtrack function with the given array, an empty path list,
# and the permutations list.
# The backtrack function is a recursive function that takes the array,
# the current path, and the permutations list as arguments.
# If the array is empty, we add the current path to the permutations list and return.


nums = [1, 2, 3]
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3],
# [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(Solution().permute(nums))
