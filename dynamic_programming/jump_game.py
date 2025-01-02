# 55. Jump Game
# Medium
# Topics
# Companies
# You are given an integer array nums.
# You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.


# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        last_position = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            max_jump = i + nums[i]
            if max_jump >= last_position:
                last_position = i

        return last_position == 0

    # Time complexity: O(n)
    # Space complexity: O(1)


# test cases to validate the solution
# test case 1
sol = Solution()
print(sol.canJump([2, 3, 1, 1, 4]))  # True
# test case 2
print(sol.canJump([3, 2, 1, 0, 4]))  # False
# test case 3
print(sol.canJump([2, 0]))  # True

# test case 4
print(sol.canJump([0]))  # True
# test case 5
print(sol.canJump([1]))  # True
