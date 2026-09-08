class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if digits == "":
            return res
        
        mp = {"2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"}
        def backtrack(index, s):
            if len(s) == len(digits):
                res.append(s)
                return 
            opts = mp[digits[index]]
            for c in opts:
                backtrack (index +1, s+c)
        
        
        
        backtrack(0, "")
        return res

        

        