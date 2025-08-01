class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        while n > 0:
            index = m+n-1
            if nums1[m-1] > nums2[n-1] and m>0:
                nums1[index] = nums1[m-1]
                m -= 1
            else:
                nums1[index] = nums2[n-1]
                n -= 1
        
        