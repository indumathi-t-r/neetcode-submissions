class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        # mapS, mapT = {},{}
        # for i in range(len(s)):
        #     mapS[s[i]] = mapS.get(s[i],0) + 1
        #     mapT[t[i]] = mapT.get(t[i],0) + 1
        
        # return mapS == mapT

        count = [0] *26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] +=1
            count[ord(t[i]) - ord('a')] -=1
        
        for j in count:
            if j!=0:
                return False
            
        return True
        