# 402. Remove K Digits
# Medium
# Topics
# Companies
# Given string num representing a non-negative integer num, and an integer k,
# return the smallest possible integer after removing k digits from num.


# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
# which is the smallest.
# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:

# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.


# Constraints:

# 1 <= k <= num.length <= 105
# num consists of only digits.
# num does not have any leading zeros except for the zero itself.

def remove_kdigits(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    stack = []
    for digit in num:
        while k and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    stack = stack[:len(stack) - k]
    res = "".join(stack)
    return str(int(res)) if res else "0"

# Time: O(N)
# Space: O

# The idea is to remove the first digit that is larger than the next one.
# We can use a stack to keep track of the digits that we have seen so far.
# We can remove the last element of the stack if the current element is smaller than the last element.
# We can repeat this process until we have removed k elements or we have reached the end of the string.
# We can then return the string formed by the remaining elements in the stack.
# We can remove any leading zeros from the resulting string.

# The time complexity is O(N) where N is the length of the string num.
# The space complexity is O(N) where N is the length of the string num.

# The code can be simplified by using a list instead of a stack.
# We can remove the last element of the list by using the pop() method.


print(remove_kdigits("1432219", 3))  # "1219"
