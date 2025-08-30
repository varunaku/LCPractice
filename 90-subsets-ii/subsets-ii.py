class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # right side == nothing
        # left side is add another.

        # pre-sort O(n * logn) 
        nums.sort()
        res = []

        def dfs(subset, i):
            if i == len(nums):
                res.append(subset.copy())
            if i >= len(nums):
                return
            # add subset
            subset.append(nums[i])
            #dfs
            dfs(subset, i+1)
            #recurse
            subset.pop()

            # now there is a chance that the next or multiple nexts are equal value
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            dfs(subset, i+1)
        
        dfs([], 0)
        return res