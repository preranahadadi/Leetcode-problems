class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        maxi = 0 
        l = 0 

        for r in range(len(s)):
            hmap[s[r]] = 1 + hmap.get(s[r],0)
            maxf = max(hmap.values())
            
            while (r-l+1) - maxf > k :
                hmap[s[l]] -= 1 
                l+=1
        
            maxi = max(maxi,r-l+1)
        return maxi 
    