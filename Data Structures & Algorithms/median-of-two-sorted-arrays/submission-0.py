from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to guarantee O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            # Partition nums1
            i = (left + right) // 2
            # Partition nums2 to ensure left half has (m + n + 1) // 2 elements
            j = (m + n + 1) // 2 - i
            
            # Handle edge cases with -inf and inf
            maxLeft1 = float('-inf') if i == 0 else nums1[i - 1]
            minRight1 = float('inf') if i == m else nums1[i]
            
            maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
            minRight2 = float('inf') if j == n else nums2[j]
            
            # Check if we found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If total length is odd, median is the max of the left halves
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                # If total length is even, median is the average of max of left and min of right
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            
            # If maxLeft1 is too big, we need to move the partition in nums1 to the left
            elif maxLeft1 > minRight2:
                right = i - 1
                
            # If maxLeft2 is too big, we need to move the partition in nums1 to the right
            else:
                left = i + 1
                
        raise ValueError("Input arrays are not sorted or invalid.")