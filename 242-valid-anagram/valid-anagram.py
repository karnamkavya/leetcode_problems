class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s)==sorted(t)
        if len(s)!=len(t):
            return False
        alpha=[0]*26
        for ch in s:
            alpha[ord(ch)-ord('a')]+=1
        for ch in t:
            if alpha[ord(ch)-ord('a')]==0:
              return False
            alpha[ord(ch)-ord('a')]-=1
        return True
