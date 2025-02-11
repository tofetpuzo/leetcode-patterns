# 45. Jump Game II
# Medium
# Topics
# Companies
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words,
# if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].


# Example 1:

# Input: nums = [2, 3, 1, 1, 4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2, 3, 0, 1, 4]
# Output: 2


# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.6M
# Submissions
# 3.8M
# Acceptance Rate
# 41.0%
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        jumps = 0
        current_reach = 0
        farthest_reach = 0
        for i in range(n - 1):  # iterate up to the second-to-last index
            # calculate the farthest reach
            farthest_reach = max(farthest_reach, i + nums[i])

            # if we've reached the limit of our current reach,make a new jump
            if i == current_reach:  # check to see if the current reach has been reached
                jumps += 1
                current_reach = farthest_reach  # update the current reach
                # check if we can reach the destination or not
                if current_reach >= n - 1:
                    return jumps

        return jumps


# Time complexity: O(n)
# Space complexity: O(1)

nums1 = [2, 3, 1, 1, 4]
nums2 = [2, 3, 0, 1, 4]
print(Solution().jump(nums1))  # 2
print(Solution().jump(nums2))  # 2
