class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res =[]
        temp = []

        def backtrack(index):
            if index == len(s):
                res.append(temp.copy())
                return
            for i in range(index,len(s)):
                if self.is_pallindrome(s,index,i):
                    temp.append(s[index:i+1])
                    backtrack(i+1)
                    temp.pop()

        
        backtrack(0)
        return res

    
    def is_pallindrome(self,s,start,end):
        while(start<=end):
            if s[start]!=s[end]:
                return False
            start +=1
            end -=1
        
        return True

        