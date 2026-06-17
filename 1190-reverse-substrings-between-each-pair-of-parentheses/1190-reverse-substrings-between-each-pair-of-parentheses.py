class Solution:
    def reverseParentheses(self, s: str) -> str:
        st=[]
        ans=""
        for i in s:
            if i=="(":
                st.append(ans)
                ans=""
            elif i==")":
                ans=st.pop()+ans[::-1]
            else:
                ans+=i
        return ans