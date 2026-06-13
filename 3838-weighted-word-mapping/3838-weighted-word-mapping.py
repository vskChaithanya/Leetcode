class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=""
        for i in words:
            count=0
            for j in i:
                index = ord(j) - ord('a')
                count+=weights[index]
            remainder=count % 26
            mapped_char = chr(ord('z') - remainder)
            ans+=mapped_char
        return ans