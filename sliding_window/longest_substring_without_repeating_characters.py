# 3. Longest Substring Without Repeating Characters
# Medium
# Topics
# Companies
# Hint
# Given a string s, find the length of the longest
# substring
# without repeating characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.
def length_of_longest_substring(s):
    """
        :type s: str
        :rtype: int
    """

    from collections import defaultdict

    window_start = 0
    max_length = 0
    char_index_map = defaultdict(int)

    "a bcabcbb"  # 3
    "l  r"

    for window_end in range(len(s)):
        right_char = s[window_end]

        if right_char in char_index_map:
            window_start = max(window_start, char_index_map[right_char] + 1)

        char_index_map[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)

    return max_length

# Time complexity: O(N)
# Space complexity: O(N)


# Example 1:
s = "abcabcbb"
print(length_of_longest_substring(s))  # 3


def length_substring(s):
    """
    type s: str"""

    set_char = set()
    window_start = 0
    n = len(s)
    max_length = 0
    for r in range(n):
        while s[r] in set_char:
            set_char.remove(s[window_start])
            window_start += 1

        set_char.add(s[r])

        max_length = max(max_length, r - window_start + 1)

    return max_length

# Time complexity: O(N)
# Space complexity: O(N)


# Example 1:
s = "abcabcbb"
print(length_substring(s))  # 3
