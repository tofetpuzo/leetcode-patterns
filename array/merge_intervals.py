# 56. Merge Intervals
# Medium
# Topics
# Companies
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


# Example 1:

# Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]
# Explanation: Since intervals[1, 3] and [2, 6] overlap, merge them into[1, 6].
# Example 2:

# Input: intervals = [[1, 4], [4, 5]]
# Output: [[1, 5]]
# Explanation: Intervals[1, 4] and [4, 5] are considered overlapping.


# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

def merge(intervals):
    """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
    intervals = sorted(intervals, key=lambda x: x[0])
    res = []
    if not intervals:
        return []

    for interval in intervals:
        if not res or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            new_res = max(res[-1][1], interval[1])
            res[-1][1] = new_res
    return res


# Time complexity: O(nlogn)
# Space complexity: O(n)

# test cases to validate the solution
# test case 1

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))
# Output: [[1, 6], [8, 10], [15, 18]]
