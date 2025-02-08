# Find the largest subarray with sum 0
# Function to find the length of the
# largest subarray with sum 0
def max_len(arr):

    n = len(arr)

    # Initialize the result
    max_len = 0

    # Loop through each starting point
    for i in range(n):

        # Initialize the current sum for
        # this starting point
        curr_sum = 0

        # Try all subarrays starting from 'i'
        for j in range(i, n):

            # Add the current element to curr_sum
            curr_sum += arr[j]

            # If curr_sum becomes 0, update max_len if required
            if curr_sum == 0:
                max_len = max(max_len, j - i + 1)

    return max_len


# arr = [15, -2, 2, -8, 1, 7, 10, 23]
# print(max_len(arr))

print(max_len([15, -2, 2, -8, 1, 7, 10, 23]))  # 5
print(max_len([1, 2, 3]))  # 0
print(max_len([1, 0, 3]))  # 2
