class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for i in asteroids:
            while st and i<0 and st[-1]>0:
                diff=i+st[-1]
                if diff<0:
                    st.pop()
                elif diff>0:
                    i=0
                else:
                    i=0
                    st.pop()
            if i:
                st.append(i)
        return st