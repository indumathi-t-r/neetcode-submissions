class Solution:
    def isHappy(self, n: int) -> bool:

        n_st = set()
        n_st.add(n)

        while n!= 1:

            res = 0
            while n:
                r = n%10
                res += r*r
                n = n//10
            n = res
            
            if n in n_st:
                return False
            n_st.add(n)
        return True