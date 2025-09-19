class Solution:
    def compress(self, chars: List[str]) -> int:

        w,r=0,0
  
        while r < len(chars):
            count = 0
            curr = chars[r]
            while r < len(chars) and chars[r] == curr:
                r+=1
                count+=1
                chars[w] = curr
            w+=1
            
            if count > 1:
                for c in str(count):
                    chars[w] = c
                    w+=1
        return w