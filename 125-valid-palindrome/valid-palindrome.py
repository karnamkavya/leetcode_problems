class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""

        for ch in s:
            if ch.isalpha() or ch.isdigit():
                clean += ch

        clean = clean.lower()
        rev = clean[::-1]

        if clean == rev:
            return True
        else:
            return False