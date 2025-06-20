class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        l = 0
        r = len(nums) - 1
        [4,5,6,0,1,2,3]
        while l <= r:
            if nums[l] < nums[r]:
                result = min(nums[l], result)
                
            m = (l+r) // 2
            result = min(nums[m], result)

            if nums[m] >= nums[l]:
                l = m + 1
            else: 
                r = m - 1

        return result