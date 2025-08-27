class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # outputting a result list of lists
        res = []
        #visited = set()

        def dfs(index, curr):

            #termination condition    
            if index == len(nums):
                res.append(curr.copy())
                return

            # then try new case, 

            curr.append(nums[index])
            # then backtrack.
            dfs(index+1, curr)
            curr.pop()
            dfs(index+1, curr)
            

        dfs(0, [])

        return res