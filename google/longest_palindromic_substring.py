# 5. Longest Palindromic Substring
# Medium
# Topics
# Companies
# Hint
# Given a string s, return the longest
# palindromic

# substring
#  in s.


# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"


# Constraints:


# 1 <= s.length <= 1000
# s consist of only digits and English letters.
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""

        start = 0
        end = 0

        # expand the string
        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            len1 = expand(s, i, i)
            len2 = expand(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start : end + 1]


print(Solution().longestPalindrome("babad"))  # bab
# print(Solution().longestPalindrome("cbbd"))  # bb
# print(Solution().longestPalindrome("a"))  # a
# print(Solution().longestPalindrome("ac"))  # a
