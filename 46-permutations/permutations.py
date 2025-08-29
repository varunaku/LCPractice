class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # with used list, we mark 0 for unused, and 1 for used

        def finder(perm, used):
            # terminating condition
                # len(perm) == len(nums)
                #res.append()
                #return
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            # iterate through each num
            for i in range(len(used)): 
                # at each point use the first number that is not used
                if used[i] == 0:    
                    # mark it as taken 
                    used[i] = 1
                    # add to permutation
                    perm.append(nums[i])
                    # call func
                    finder(perm, used)
                    # pop and undo used_arr changes
                    perm.pop()
                    used[i] = 0
      
                # next iteration of for loop, for all n

        finder([], [0] * len(nums))       
            
        return res