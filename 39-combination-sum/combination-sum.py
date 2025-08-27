class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, current_combo, total):
            # start at the current index, and add as many as you can before you over shoot
            if total == target:
                res.append(current_combo.copy())
                return
            if total > target:
                return
            if index > len(nums)-1:
                return

            current_combo.append(nums[index]) 

            dfs(index, current_combo, total+ nums[index])
            current_combo.pop()
            dfs(index+1, current_combo, total)
            
        dfs(0, [], 0)
        return res