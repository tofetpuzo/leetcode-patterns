# 30. Substring with Concatenation of All Words
# Hard
# Topics
# conpanies icon
# Companies
# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

# Example 1:

# Input: s = "barfoothefoobarman", words = ["foo","bar"]

# Output: [0,9]

# Explanation:

# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

# Example 2:

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

# Output: []

# Explanation:

# There is no concatenated substring.

# Example 3:

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

# Output: [6,9,12]

# Explanation:

# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

# Constraints:

# 1 <= s.length <= 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# s and words[i] consist of lowercase English letters.

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        # Step 1: Handle edge cases and get basic measurements
        if not s or not words or not words[0]:
            return []
        
        word_len = len(words[0])  # Length of each word
        total_words = len(words)  # Number of words
        total_len = word_len * total_words  # Total length of concatenated string
        
        # If string is shorter than total length needed, no solution
        if len(s) < total_len:
            return []
        
        # Step 2: Create frequency map of words we need to find
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        result = []
        
        # Step 3: Only need to check word_len different starting positions
        # This is the key optimization - instead of checking every position,
        # we only check positions 0, 1, 2, ..., word_len-1
        for i in range(word_len):
            self._sliding_window_check(s, i, word_len, total_words, word_count, result)
        
        return result
    
    def _sliding_window_check(self, s, start, word_len, total_words, word_count, result):
        """
        Use sliding window to check all possible concatenations starting at positions
        start, start + word_len, start + 2*word_len, etc.
        """
        seen = {}  # Count of words in current window
        left = start  # Left boundary of window
        
        # Slide through string with step size = word_len
        for right in range(start, len(s) - word_len + 1, word_len):
            # Extract current word
            word = s[right:right + word_len]
            
            # If word is not in our target words, reset window
            if word not in word_count:
                seen.clear()
                left = right + word_len
                continue
            
            # Add word to current window
            seen[word] = seen.get(word, 0) + 1
            
            # If we have too many of this word, shrink window from left
            while seen[word] > word_count[word]:
                left_word = s[left:left + word_len]
                seen[left_word] -= 1
                if seen[left_word] == 0:
                    del seen[left_word]
                left += word_len
            
            # Check if current window contains exactly what we need
            if right - left + word_len == total_words * word_len:
                result.append(left)
