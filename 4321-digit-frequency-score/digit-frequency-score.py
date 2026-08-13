class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        n = str(n)
        total = 0
        for i in range(len(n)):
            total += int(n[i])  
        return total
