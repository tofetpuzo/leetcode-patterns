# 739. Daily Temperatures
# Medium
# Topics
# Companies
# Hint
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days
# you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.


# Example 1:

# Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# Output: [1, 1, 4, 2, 1, 1, 0, 0]
# Example 2:

# Input: temperatures = [30, 40, 50, 60]
# Output: [1, 1, 1, 0]
# Example 3:

# Input: temperatures = [30, 60, 90]
# Output: [1, 1, 0]


# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100
def dailyTemperatures(temperatures):
    """
        :type temperatures: List[int]
        :rtype: List[int]
    """
    stack = []
    res = [0] * len(temperatures)
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            cur = stack.pop()
            res[cur] = i - cur
        stack.append(i)
    return res

# Time complexity: O(n)
# Space complexity: O(n)


# test case
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# Output: [1, 1, 4, 2, 1, 1, 0, 0]

print(dailyTemperatures(temperatures))
# test case
temperatures = [30, 40, 50, 60]
# Output: [1, 1, 1, 0]

print(dailyTemperatures(temperatures))
# test case
temperatures = [30, 60, 90]
# Output: [1, 1, 0]

print(dailyTemperatures(temperatures))


# approach 2

def dailyTemperatures(temperatures):
    """
        :type temperatures: List[int]
        :rtype: List[int]
    """
    stack = []
    res = [0] * len(temperatures)
    for i, t in enumerate(temperatures):
        while stack and stack[-1][0] < t:
            stack_t, stack_i = stack.pop()
            res[stack_i] = i - stack_i
        stack.append((t, i))
    return res


# test case
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# Output: [1, 1, 4, 2, 1, 1, 0, 0]

print(dailyTemperatures(temperatures))
# test case
temperatures = [30, 40, 50, 60]
# Output: [1, 1, 1, 0]

print(dailyTemperatures(temperatures))
# test case
temperatures = [30, 60, 90]
# Output: [1, 1, 0]

print(dailyTemperatures(temperatures))
