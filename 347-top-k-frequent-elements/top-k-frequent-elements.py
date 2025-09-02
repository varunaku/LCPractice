class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #[1,2,2,3,3,3] k = 2
        #2,3
        buckets = [[] for i in range(len(nums)+1)] 
        # as freq can go up to len(nums), we'll add one
        occ = {}
        res = []
        # only one pass through the array at a time
        # nums can be positive or negative
        # can be 0 or more occurances
        # can use a hash map, and add into hash map as you increment
        for i in range(len(nums)):
            occ[nums[i]] = occ.get(nums[i], 0) + 1 
        for key, val in occ.items():
            # buckets[0] -> 0 frequency
            # buckets[1] -> 1 frequency
            # buckets[2] -> 2 frequency
            # buckets[val] = key
            buckets[val].append(key)
            #key = nums[i] value, val = nums[i] frequency
        # is array sorted? 
        print(buckets)

        for i in range(len(nums), -1, -1):
            bucket = len(buckets[i])
            while bucket > 0 and k > 0:
                res.append(buckets[i][bucket-1])
                bucket -= 1
                k -= 1
                
        return res