class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = [0] *26
        s2map =[0] *26
        l,r = 0,0

        if len(s1)> len(s2):
            return False
        
        while (r< len(s1)):
            s1map[ord(s1[r])-ord('a')] += 1
            s2map[ord(s2[r])-ord('a')] += 1
            r +=1 
        
        while (r<len(s2)):
            if s1map == s2map:
                return True
            
            s2map[ord(s2[r])- ord('a')] +=1

            s2map[ord(s2[l])- ord('a')] -=1
            l +=1
            r +=1
        return s2map ==s1map




        