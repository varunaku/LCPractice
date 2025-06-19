class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        # d = {}
        # l = 0
        # length = 0
        # total_length = 0

        # for i in range(len(s)):
        #     if s[i] in d:
        #         l = max(l, d[s[i]] + 1)
                
        #     d[s[i]] = i
        #     length = i - l + 1
        #     total_length = max(length, total_length)

        # return total_length

        substringlength = 0
        l = 0
        r = 1
        if len(s) <= 1:
            return len(s)

        hashy = {s[l]: 0}

        while r < len(s):
            # if not in hashmap, add.
            if s[r] not in hashy:
                hashy[s[r]] = r # 'c' = index
            else: 
                if hashy[s[r]]+1 > l:
                    l = hashy[s[r]]+1  
                hashy[s[r]] = r
                # never move backwards, that could happen.
            substringlength = max(substringlength, r-l+1)
            r+=1

        return substringlength


        