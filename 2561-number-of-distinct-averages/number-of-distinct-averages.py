class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avg=set()
        nums.sort()

        while nums:
            s=nums.pop(0)
            l=nums.pop(-1)
            a=(s+l)/2
            avg.add(a)

        return len(avg)
        
        
