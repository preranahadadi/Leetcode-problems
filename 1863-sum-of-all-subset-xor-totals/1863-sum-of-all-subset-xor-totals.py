class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i , total):
            if i == len(nums):
                return total
            pick = dfs(i+1,total^nums[i])
            unpick = dfs(i+1,total)
            return pick+unpick
            
        return dfs(0,0)