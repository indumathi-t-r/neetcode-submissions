class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = {}

        if len(t) > len(s):
            return ""
        
        for ch in t:
            mp[ch] = mp.get(ch,0)+1
        
        l,r = 0,0
        start_idx = 0
        min_wl,cur_wl = float("inf"), 0
        req_cnt = len(t)

        while(r<len(s)):
            if s[r] in mp:
                if mp[s[r]]>0:
                    req_cnt -=1
                mp[s[r]] -=1
            while (req_cnt == 0):
                cur_wl = r-l+1
                if (cur_wl<min_wl):
                    min_wl = cur_wl
                    start_idx = l
                if s[l] in mp:
                    mp[s[l]] +=1
                    if (mp[s[l]]>0):
                        req_cnt +=1
                l +=1

            r +=1
        return "" if min_wl == float("inf") else s[start_idx:min_wl +start_idx ]



        