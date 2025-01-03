# 1189. Maximum Number of Balloons
# Easy
# Topics
# Companies
# Hint
# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.


# Example 1:


# Input: text = "nlaebolko"
# Output: 1
# Example 2:


# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0


# Constraints:

# 1 <= text.length <= 104
# text consists of lower case English letters only.


# Note: This question is the same as 2287: Rearrange Characters to Make Target String.
import test


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        from collections import defaultdict

        ball = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        freq = defaultdict(int)
        for c in text:
            freq[c] += 1
        return min(freq[char] // count for char, count in ball.items())


def max_balloons(text):
    ball = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
    balloons_made = 0

    # Convert text to a dictionary of counts
    temp_text = {}
    for char in text:
        temp_text[char] = temp_text.get(char, 0) + 1

    while True:
        possible = True
        for char, count in ball.items():
            if temp_text.get(char, 0) < count:
                possible = False
                break

        if not possible:
            break

        for char, count in ball.items():
            temp_text[char] -= count
        balloons_made += 1

    return balloons_made


text = {"b": 2, "a": 8, "l": 8, "o": 8, "n": 8}
print(max_balloons(text))  # output 2
text = {"b": 3, "a": 8, "l": 8, "o": 8, "n": 8}
print(max_balloons(text))  # output 3
text = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
print(max_balloons(text))  # output 1
text = {"b": 0, "a": 8, "l": 8, "o": 8, "n": 8}
print(max_balloons(text))  # output 0


# Time: O(N)
# Space: O(N)

text = "loonbalxballpoon"
print(Solution().maxNumberOfBalloons(text))  # 2
