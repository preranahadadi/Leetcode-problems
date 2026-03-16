class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for i in stones:
            heapq.heappush(maxheap,-i)
        
        while len(maxheap)>1:
            x = -heapq.heappop(maxheap)
            y = -heapq.heappop(maxheap)
            if x > y:
                total = -(x-y)
                heapq.heappush(maxheap, total) 
        return -heapq.heappop(maxheap) if maxheap else 0