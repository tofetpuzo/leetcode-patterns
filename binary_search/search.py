from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Time: O(logN)
# Space: O(1)

# example 1
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target))  # 4


def search_alt(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    mid = (left + right) // 2

    while left <= right:
        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        mid = (left + right) // 2

    return -1


print(search_alt(nums, target))  # 4
