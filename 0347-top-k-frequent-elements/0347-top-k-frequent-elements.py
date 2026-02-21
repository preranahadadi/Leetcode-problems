class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            hmap[nums[i]] = 1+hmap.get(nums[i],0)

        bucket = [[] for i in range(len(nums)+1)]
        for num,cnt in hmap.items():
            bucket[cnt].append(num)
        
        res = []
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res 

        