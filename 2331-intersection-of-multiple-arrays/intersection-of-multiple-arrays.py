from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        set1 = set(nums[0])  
        for row in nums[1:]:  
            set1 = set1.intersection(set(row)) 
        li = list(set1)
        li.sort()
        return li
