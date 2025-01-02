# 746. Min Cost Climbing Stairs
# Easy
# Topics
# Companies
# Hint
# You are given an integer array cost
# where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.


# Example 1:

# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
# Example 2:

# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.


# Constraints:

# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999

# using recursive approach

def min_cost_climbing_stairs(cost):
    n = len(cost)

    memo = {0: 0, 1: 0}

    def min_cost(i):
        if i in memo:
            return memo[i]
        memo[i] = cost[i] + min(min_cost(i-1), min_cost(i-2))
        return memo[i]

    return min_cost(n)


class Solution(object):
    def min_cost_climbing_Stairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * len(cost) + 1

        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[len(cost)]

    # using constant space
    def min_cost_climbing_stairs(self, cost):
        prev = curr = 0
        for i in range(2, len(cost) + 1):
            prev, curr = curr, min(prev + cost[i-1], curr + cost[i-2])

        return curr
    # using constant space
