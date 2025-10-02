# 172. Factorial Trailing Zeroes
# Medium
# Topics
# conpanies icon
# Companies
# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

# Example 1:

# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:

# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Example 3:

# Input: n = 0
# Output: 0
 

# Constraints:

# 0 <= n <= 104

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        # Count the number of factors of 5 in n!
        # 
        # WHY THIS WORKS:
        # Trailing zeros are created by factors of 10, and 10 = 2 × 5
        # In any factorial n!, there are always more factors of 2 than factors of 5
        # So the number of trailing zeros = number of pairs of (2,5) = number of factors of 5
        #
        # EXAMPLES:
        # 5! = 120 has one factor of 5 (from 5) → 1 trailing zero
        # 10! = 3,628,800 has factors of 5 from: 5, 10 → 2 factors of 5 → 2 trailing zeros  
        # 25! has factors of 5 from: 5,10,15,20,25 → but 25=5² contributes 2 factors → total 6
        #
        # ALGORITHM:
        # n//5 gives multiples of 5: 5,10,15,20,25,30...
        # n//25 gives multiples of 25: 25,50,75... (each contributes extra factor of 5)
        # n//125 gives multiples of 125: 125,250... (each contributes another extra factor)
        # We keep dividing by 5 to count all these contributions
        while n >= 5:
            n //= 5
            count += n
        return count
 
