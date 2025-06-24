class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = set()
        # |i - j| <= k
        # nums[j] == key

        # return all sorted ascending
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if abs(i - j) <= k and nums[j] == key:
        #             res.add(i)


        # return list(res)

        # alternatively, break into 2 loops. First loop is to find all key indexes and store
        # 2nd loop is to iterate through the 
        n = len(nums)
        for j in range(len(nums)):
            if nums[j] == key:
                start_bound = max(0, j-k) # to ensure no index below zero
                end_bound = min(n-1, j+k)
                for i in range(start_bound, end_bound+1):
                    res.add(i)

        return list(res)
        # best solution. find difference from each key index (j) or +k / -k, and add both to set. 
        # o(n) This way only one iteraiton needed.