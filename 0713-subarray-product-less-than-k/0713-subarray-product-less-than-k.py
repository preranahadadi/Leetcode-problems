class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l , r = 0,0
        cnt = 0 
        prod = 1 
        if k == 0 : 
            return 0 
        if k == 1 : 
            return 0
        for r in range(len(nums)):
            prod = prod * nums[r]
            while prod >= k:
                prod = prod // nums[l]
                l = l + 1 
            cnt = cnt + (r-l+1) 
        return cnt
        