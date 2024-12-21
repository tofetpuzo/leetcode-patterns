# 42. Trapping Rain Water
# Hard
# Topics
# Companies
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


# Example 1:


# Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6
# Explanation: The above elevation map(black section) is represented by array[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]. In this case, 6 units of rain water(blue section) are being trapped.
# Example 2:

# Input: height = [4, 2, 0, 3, 2, 5]
# Output: 9


# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

def trap(height):
    """
         :type height: List[int]
         :rtype: int
    """
    l_wall = r_wall = 0
    n = len(height)
    max_wall_left = [0] * n
    max_wall_right = [0] * n

    for i in range(n):
        j = -i - 1
        max_wall_left[i] = l_wall
        max_wall_right[j] = r_wall

        l_wall = max(l_wall, height[i])
        r_wall = max(r_wall, height[j])

    sum_water = 0
    for i in range(n):
        water = min(max_wall_left[i], max_wall_right[i]) - height[i]
        if water > 0:
            sum_water += water

    return sum_water    

# Time complexity: O(n)
# Space complexity: O(n)

# test case
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))  # 6