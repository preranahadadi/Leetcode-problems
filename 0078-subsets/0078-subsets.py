class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = [] 
        res = [] 

        def dfs(i, res) : 
            if i  == len(nums) : 
                ans.append(res)
                return 


            pick = dfs(i+1, res + [nums[i]]) 
            nonpick = dfs(i+1, res) 

        dfs(0, res)
        return ans 
        