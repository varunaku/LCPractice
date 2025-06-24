class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = set()
        # |i - j| <= k
        # nums[j] == key

        # return all sorted ascending
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i - j) <= k and nums[j] == key:
                    res.add(i)


        return list(res)