class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 
            
            # case where we pick the number
            subset.append(nums[i])
            dfs(i+1)

            #case where you don't pick the number
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
