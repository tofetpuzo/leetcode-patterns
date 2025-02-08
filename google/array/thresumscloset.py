# 16. 3Sum Closest
# Attempted
# Medium
# Topics
# Companies
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.


# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


# Constraints:


# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104


class Solution(object):
    def threeSumClosest(self, nums: list, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_sum = float("inf")
        closest_diff = float("inf")
        n = len(nums)
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                diff = abs(current_sum - target)
                if diff < closest_diff:
                    closest_diff = diff
                    closest_sum = current_sum
                if current_sum == target:
                    return current_sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum


nums = [-1, 2, 1, -4]
target = 1
print(Solution().threeSumClosest(nums, target))
# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
