# 322. Coin Change
# Medium
# Topics
# Companies
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.


# Example 1:

# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0


# Constraints:


# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # first approach: dynamic programming
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1

        # second approach: memoization

    def dfs(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = {}

        def helper(remaining):
            if remaining < 0:
                return float("inf")
            if remaining == 0:
                return 0
            if remaining in memo:
                return memo[remaining]

            min_coins = float("inf")
            for coin in coins:
                res = helper(remaining - coin)
                if res != float("inf"):
                    min_coins = min(min_coins, res + 1)

            memo[remaining] = min_coins
            return min_coins

        result = helper(amount)
        return result if result != float("inf") else -1


# Example usage:
sol = Solution()
print(sol.coinChange([1, 2, 5], 11))  # Output: 3
print(sol.coinChange([2], 3))  # Output: -1
print(sol.coinChange([1], 0))  # Output: 0
print(sol.coinChange([1, 2, 5], 100))  # Output: 20
print(sol.coinChange([186, 419, 83, 408], 6249))  # Output: 20
# print(sol.dfs([1, 2, 5], 11))  # Output: 3


# # Example usage:
print(sol.dfs([1, 2, 5], 100))  # Output: 20
print(sol.dfs([186, 419, 83, 408], 6249))  # Output: 20
