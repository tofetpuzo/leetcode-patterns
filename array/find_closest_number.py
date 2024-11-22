# Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

 

# Example 1:

# Input: nums = [-4,-2,1,4,8]
# Output: 1
# Explanation:
# The distance from -4 to 0 is |-4| = 4.
# The distance from -2 to 0 is |-2| = 2.
# The distance from 1 to 0 is |1| = 1.
# The distance from 4 to 0 is |4| = 4.
# The distance from 8 to 0 is |8| = 8.
# Thus, the closest number to 0 in the array is 1.
# Example 2:

# Input: nums = [2,-1,1]
# Output: 1
# Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
 

# Constraints:

# 1 <= n <= 1000
# -105 <= nums[i] <= 105

from os import close


def find_closest_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    closest_number = float('inf')
    
    if not nums:
        return closest_number
    
    for num in nums:
        if abs(num) < abs(closest_number):
            closest_number = num
        elif abs(num) == abs(closest_number) and num > closest_number:
            closest_number = num
    return closest_number

# Time complexity: O(n)
# Space complexity: O(1)

# test case
nums = [-4,-2,1,4,8]
# Output: 1
print(find_closest_number(nums))

# test case
nums = [2,-1,1]
# Output: 1
print(find_closest_number(nums))
