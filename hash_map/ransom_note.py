# 383. Ransom Note
# Easy
# Topics
# Companies
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.


# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true


# Constraints:


# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import defaultdict

        info = defaultdict(int)
        rans = defaultdict(int)

        for letter in magazine:
            info[letter] += 1

        for i in ransomNote:
            rans[i] += 1

        for key in rans:
            if rans[key] > info[key]:
                return False

        return True


ransomNote = "aa"
magazine = "aab"
print(Solution().canConstruct(ransomNote, magazine))
