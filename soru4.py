"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.


Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

def median(l1:list,l2:list):
    l3 = l1 + l2
    length = len(l3)

    if (length % 2) == 0:
        m_index = int((length / 2) - 1)
        n_index = m_index + 1 
        result = (l3[m_index] + l3[n_index]) / 2
        print(result)
    
    elif (length % 2) != 0:
        m_index = int(((length + 1) / 2) - 1)
        result = l3[m_index]
        print(result)
        

nums1 = [1,2,3,5]
nums2 = [3,4,5]

median(nums1,nums2)























