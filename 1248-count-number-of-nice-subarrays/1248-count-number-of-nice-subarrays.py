from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k: int) -> int:
            l = 0
            cnt = 0
            ans = 0

            for r in range(len(nums)):
                if nums[r] % 2 == 1:
                    cnt += 1

                while cnt > k:
                    if nums[l] % 2 == 1:
                        cnt -= 1
                    l += 1

                ans += (r - l + 1)

            return ans

        return atMost(k) - atMost(k - 1)