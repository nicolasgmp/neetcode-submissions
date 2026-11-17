class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k = 0 
        maxLen = 0
        res = set()
        for i, c in enumerate(s):
            while c in res:
                res.remove(s[k])
                k+=1
            res.add(c)
            maxLen = max(i - k + 1, maxLen)
        return maxLen