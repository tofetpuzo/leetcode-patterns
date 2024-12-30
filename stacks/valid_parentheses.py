# 20. Valid Parentheses
# Easy
# Topics
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            print(char)
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
    

print(is_valid("()")) # True`
# print(is_valid("()[]{}")) # True
# print(is_valid("(]")) # False`



def is_alt_valid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char not in mapping:
            stack.append(char) 
            
        else:
            if not stack:
                return False
            top_element = stack.pop()
            if mapping[char] != top_element:
                return False
    return not stack

print(is_alt_valid("()")) # True`
print(is_alt_valid("()[]{}")) # True
print(is_alt_valid("(]")) # False`