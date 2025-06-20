class Solution:
    def search(self, nums: List[int], target: int) -> int:
        output = -1
        l,r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2  

            if nums[mid] == target:
                return mid  

            # IMPORTANT: IF MID >= L, then Left side is sorted part including mid
            if nums[mid] >= nums[l]: # left portion is sorted [3,4,5,6,1,2]
                if target > nums[mid] or target < nums[l]: 
                    # go to right portion 
                    l = mid + 1
                else:
                    # go to the left portion
                    r = mid - 1 

            else: # right portion is sorted [6,1,2,3,4,5]
                if target < nums[mid] or target > nums[r]:
                    # left portion
                    r = mid - 1
                else: 
                    #right portion
                    l = mid + 1
  
        return output