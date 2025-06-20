class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_contents = {} # store the contents
        # determine what letters of t are already in window
        window_letter_count = 0 # how many letters in T have atleast one occurrence in the s window
        # should be equal to length of t
        countT = Counter(t)  # ✅ required character frequencies

        need = len(countT)  

        window_size = len(s) +1 # min()
        final_l = 0
        final_r = 0
        # iterate through s
        # l pointer is initially zero
        l = 0
        for r in range(len(s)):
            # fetch count val of letter
            window_contents[s[r]] = 1 + window_contents.get(s[r], 0) 

            if s[r] in countT and window_contents[s[r]] == countT[s[r]]:
                window_letter_count += 1 #update

                #print("letter identified", have, s[r], window_letter_count)

            # if we have all 3 letters, capture window size 
            # then compare to smallest window size, and set it
            #making window smaller logic
            while window_letter_count == need and l <= r:
                
                if (r - l + 1) < window_size:
                    window_size = r - l + 1
                    final_l = l
                    final_r = r + 1
                
                window_contents[s[l]] = window_contents.get(s[l], 0) - 1

                if s[l] in countT and window_contents[s[l]] < countT[s[l]]:
                    window_letter_count -= 1

                l += 1

        return s[final_l:final_r] 



