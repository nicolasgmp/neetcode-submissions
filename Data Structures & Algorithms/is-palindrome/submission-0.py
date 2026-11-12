class Solution:
    def isPalindrome(self, s: str) -> bool:
       toTest = "".join(re.sub(r'[^a-zA-Z0-9]','', s).lower())
       l, r = 0, len(toTest)-1
       while l < r:
        if toTest[l] != toTest[r]:
            return False
        l+=1
        r-=1
       return True 