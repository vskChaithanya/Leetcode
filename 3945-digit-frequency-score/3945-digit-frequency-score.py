class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        count=0
        for i in str(n):
            count += int(i)
        return count