class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setChar = set()
        l , res = 0, 0

        for r in range(len(s)):
            while s[r] in setChar:
                setChar.remove(s[l])
                l+=1
            setChar.add(s[r])
            res = max(res,r-l+1)
        return res

