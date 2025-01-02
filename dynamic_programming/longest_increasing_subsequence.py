# 300. Longest Increasing Subsequence
# Medium
# Topics
# Companies
# Given an integer array nums, return the length of the longest strictly increasing
# subsequence
# .


# Example 1:

# Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
# Output: 4
# Explanation: The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
# Example 2:

# Input: nums = [0, 1, 0, 3, 2, 3]
# Output: 4
# Example 3:

# Input: nums = [7, 7, 7, 7, 7, 7, 7]
# Output: 1


# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104


# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
# #


class Solution(object):
    def length_of_longest_increasing_subsquence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                print(i, j)
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# Time complexity: O(n^2)
# Space complexity: O(n)


# test cases to validate the solution
# test case 1
sol = Solution()
print(sol.length_of_longest_increasing_subsquence([10, 9, 2, 5, 3, 7, 101, 18]))  # 4