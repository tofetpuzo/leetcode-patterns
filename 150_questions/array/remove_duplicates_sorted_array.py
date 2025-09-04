# 26. Remove Duplicates from Sorted Array
# Solved
# Easy
# Topics
# conpanies icon
# Companies
# Hint
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

from typing import List


class Solution:                                                                                                     
    def removeDuplicates(self, nums: List[int]) -> int:                                                             
        """                                                                                                         
        Remove duplicates from sorted array in-place.                                                               
                                                                                                                    
        Args:                                                                                                       
            nums: Sorted array in non-decreasing order                                                              
                                                                                                                    
        Returns:                                                                                                    
            Number of unique elements (k)                                                                           
        """                                                                                                         
        if not nums:                                                                                                
            return 0                                                                                                
                                                                                                                    
        # Two pointer approach                                                                                      
        # k tracks the position for next unique element                                                             
        k = 1                                                                                                       
                                                                                                                    
        # Start from second element                                                                                 
        for i in range(1, len(nums)):                                                                               
            # If current element is different from previous unique element                                          
            if nums[i] != nums[k - 1]:                                                                              
                nums[k] = nums[i]                                                                                   
                k += 1                                                                                              
                                                                                                                    
        return k                                                                                                    
                                                                                                                    
# Test cases                                                                                                        
                                                                                        
solution = Solution()                                                                                           
                                                                                                                
# Test case 1                                                                                                   
nums1 = [1, 1, 2]                                                                                               
k1 = solution.removeDuplicates(nums1)                                                                           
print(f"Input: [1,1,2]")                                                                                        
print(f"Output: k = {k1}, nums = {nums1[:k1]}")                                                                 
print()                                                                                                         
                                                                                                                
# Test case 2                                                                                                   
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]                                                                          
k2 = solution.removeDuplicates(nums2)                                                                           
print(f"Input: [0,0,1,1,1,2,2,3,3,4]")     
print(f"Output: k = {k2}, nums = {nums2[:k2]}")        