# 383. Ransom Note
# Solved
# Easy
# Topics
# conpanies icon
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

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter

        # Count the frequency of each character in magazine
        magazine_count = Counter(magazine)
        
        # Check if each character in ransomNote can be constructed from magazine
        for char in ransomNote:
            if magazine_count[char] <= 0:
                return False
            magazine_count[char] -= 1
        
        return True
        

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict
        hash = defaultdict(int)
        for r in magazine:
            hash[r]+=1

        for char in ransomNote:
            if char in hash:
               hash[char]-=1
            if hash[char] <= 0:
                    return False
        return True
    
    
# Example usage:
solution = Solution()
print(solution.canConstruct("a", "b"))  # Output: False
print(solution.canConstruct("aa", "ab"))  # Output: False
print(solution.canConstruct("aa", "aab"))  # Output: True
print(solution.canConstruct2("a", "b"))  # Output: False
print(solution.canConstruct2("aa", "ab"))  # Output: False