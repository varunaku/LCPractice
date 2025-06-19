class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashy = {} 
            # counts occurence of each letter
        # longest
        longest = 0 
        # counter for what we have in current window
        longest_char_count = 0

        # if my window of size 3 has 2 of the same chars, and a k of 1, it will work
        # if my window has size 5 and 2 of the same chars and k of 2, it won't work
        # ideally: window size - max_occurence of a char <= k
        l = 0
        for r in range(len(s)):
            # when we grow window, add to the count, or add new
            hashy[s[r]] = 1 + hashy.get(s[r], 0) # get the associated value, and default to 0 if not exists
            longest_char_count = max(longest_char_count, hashy[s[r]])

            # ideally: window size - max_occurence of a char <= k
            # and if not the case, shrink window until back in range
            while (r - l + 1) - longest_char_count > k:
                # when we shrink the window, subtract from the count
                hashy[s[l]] -= 1
                # update left pointer
                l += 1

            # update solution
            longest = max(longest, r-l+1)
            
        return longest 