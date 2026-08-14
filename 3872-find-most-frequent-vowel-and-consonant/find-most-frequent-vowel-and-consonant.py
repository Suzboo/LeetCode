class Solution:
    def maxFreqSum(self, s: str) -> int:
        f={}
        f1={}
        for ch in s:
            if ch in "aeiou":
                f[ch]=f.get(ch,0)+1
            else:
                f1[ch]=f1.get(ch,0)+1
        
        if f:
            max1 = max(f.values())
        else:
            max1 = 0

        if f1:
            max2 = max(f1.values())
        else:
            max2 = 0

        return max1+max2


        return max1+max2


