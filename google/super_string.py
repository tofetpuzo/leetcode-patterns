# Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations.
#
# In each operation, select a pair of adjacent letters that match, and delete them.

# Delete as many characters as possible using this method and return the resulting string. If the final string is empty, return Empty String

# Example.


# aab shortens to b in one operation: remove the adjacent a characters.


# Remove the two 'b' characters leaving 'aa'. Remove the two 'a' characters to leave ''. Return 'Empty String'.

# Function Description

# Complete the superReducedString function in the editor below.

# superReducedString has the following parameter(s):

# string s: a string to reduce
# Returns

# string: the reduced string or Empty String
# Input Format

# A single string, .

# Constraints

# Sample Input 0

# aaabccddd
# Sample Output 0

# abd
# Explanation 0

# Perform the following sequence of operations to get the final string:

# aaabccddd → abccddd → abddd → abd
# Sample Input 1

# aa
# Sample Output 1

# Empty String

# Explanation 1
# aa → Empty String
# Sample Input 2

# baab
# Sample Output 2

# Empty String
# Explanation 2

# baab → bb → Empty String


#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

from collections import defaultdict

# Write your code here

# "aaabccddd"


def check_each_length(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return "".join(stack) if stack else ""


s = "aaabccddd"
print(check_each_length(s))
# aaabccddd → abccddd → abddd → abd
