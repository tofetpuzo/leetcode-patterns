# 346. Moving Average from Data Stream
# Easy
# Topics
# Companies
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Implement the MovingAverage class:

# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.


# Example 1:

# Input
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
# Output
# [null, 1.0, 5.5, 4.66667, 6.0]

# Explanation
# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1); // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3


# Constraints:


# 1 <= size <= 1000
# -105 <= val <= 105
# At most 104 calls will be made to next.
class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.queue = []
        self.sum = 0
        self.count = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        self.sum += val
        self.count += 1

        if self.count > self.size:
            self.sum -= self.queue.pop(0)
            self.count -= 1

        return self.sum / self.count


# Your MovingAverage object will be instantiated and called as such:
# test cases to validate the solution
# test case 1
print("test case 1")
movingAverage = MovingAverage(3)
print(movingAverage.next(1))  # return 1.0 = 1 / 1
print(movingAverage.next(10))  # return 5.5 = (1 + 10) / 2
print(movingAverage.next(3))  # return 4.66667 = (1 + 10 + 3) / 3
print(movingAverage.next(5))  # return 6.0 = (10 + 3 + 5) / 3
# test case 2
