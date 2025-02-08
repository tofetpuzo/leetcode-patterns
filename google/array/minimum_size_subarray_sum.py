# 209. Minimum Size Subarray Sum
# Attempted
# Medium
# Topics
# Companies
# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0


# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104


# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
class Solution(object):
    def min_sub_arrayLen(self, target, nums: list):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_len = float("inf")  # Initialize min_len to infinity
        left = 0
        window_sum = 0

        for right in range(n):
            window_sum += nums[right]

            while window_sum >= target:
                min_len = min(min_len, right - left + 1)  # update min length

                window_sum -= nums[left]  # remove left most and try to make it smaller
                left += 1  # move left

        return min_len if min_len != float("inf") else 0


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(
    Solution().min_sub_arrayLen(
        target,
        nums,
    )
)

nums = [1, 4, 4]
target = 4
print(
    Solution().min_sub_arrayLen(
        target,
        nums,
    )
)

nums = [1, 1, 1, 1, 1, 1, 1, 1]
target = 11
print(
    Solution().min_sub_arrayLen(
        target,
        nums,
    )
)

target = 11
nums = [1, 2, 3, 4, 5]
print(
    Solution().min_sub_arrayLen(
        target,
        nums,
    )
)

target = 15
nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
print(
    Solution().min_sub_arrayLen(
        target,
        nums,
    )
)
