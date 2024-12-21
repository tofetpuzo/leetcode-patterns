# 424. Longest Repeating Character Replacement
# Medium
# Topics
# Companies
# You are given a string s and an integer k.
# You can choose any character of the string and change it to any other uppercase
# English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter
# you can get after performing the above operations.


# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.


# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

def character_replacement(s, k):
    """
        :type s: str
        :type k: int
        :rtype: int
    """

    from collections import defaultdict

    window_start = 0
    max_length = 0
    max_repeat_letter_count = 0
    char_frequency = defaultdict(int)

    for window_end in range(len(s)):
        right_char = s[window_end]
        char_frequency[right_char] += 1

        max_repeat_letter_count = max(
            max_repeat_letter_count, char_frequency[right_char])

        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = s[window_start]
            char_frequency[left_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length

# Time complexity: O(N)

# Space complexity: O(1) since we are using a fixed size array of size 26 to store the frequency of the characters.


# Tests
s = "ABAB"
k = 2
print(character_replacement(s, k))  # 4

s = "AABABBA"
k = 1
print(character_replacement(s, k))  # 4


def character_replacements(s, k):
    