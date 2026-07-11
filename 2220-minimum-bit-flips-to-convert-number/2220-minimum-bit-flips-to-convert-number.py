class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans=start^goal
        x=bin(ans).count("1")
        return x