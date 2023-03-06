class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        r = 0 
        sub = set()
        for ch in s:
            while ch in sub:
                sub.remove(s[l])
                l += 1

            sub.add(ch)
            r += 1
            res = max(res, r-l)
        return res
        