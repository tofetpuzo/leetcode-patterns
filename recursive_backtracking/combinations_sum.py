# 9. Combination Sum
# Medium
# Topics
# Companies
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
# frequency
# of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


# Example 1:

# Input: candidates = [2, 3, 6, 7], target = 7
# Output: [[2, 2, 3], [7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2, 3, 5], target = 8
# Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []


# Constraints:

# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res, sol = [], []

        def backtrack(start, target):
            if target == 0:
                res.append(sol[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                sol.append(candidates[i])
                backtrack(i, target - candidates[i])
                sol.pop()

        backtrack(0, target)
        return res

# Time complexity: O(N^target)
# Space complexity: O(target)
# Approach: Backtracking
# The idea is to generate all the combinations of the given array that sum up to the target.
# We can do this by using backtracking.

# We start by creating an empty list called combinations.

# We then call the backtrack function with the given array, an empty path list, and the target.

# The backtrack function is a recursive function that takes the array, the path list, and the target.

# If the target is 0, we add the current path to the combinations list and return.

# Otherwise, we iterate over the array and add the current element to the path list.

# We then call the backtrack function with the updated path list and the target - current element.

# We then remove the current element from the path list and continue the loop.


# test cases
candidates = [2, 3, 6, 7]
target = 7
# Output: [[2, 2, 3], [7]]

print(Solution().combinationSum(candidates, target))


# second approach

def combinationSum(candidates, target):
    res, sol = [], []
    nums = candidates
    n = len(nums)

    def backtrack(i, curr_sum):
        if curr_sum == target:
            res.append(sol[:])
            return
        if curr_sum > target or i == n:
            return

        backtrack(i+1, curr_sum)
        sol.append(nums[i])
        backtrack(i, curr_sum + nums[i])
        sol.pop()
    backtrack(0, 0)

    return res
