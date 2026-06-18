class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans=tasks[0][0]+tasks[0][1]
        for i in tasks:
            finish=i[0]+i[1]
            if finish<ans:
                ans=finish
        return ans