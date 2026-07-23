class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''.join([char for char in s if char.isalnum()]).lower()
        return t == t[::-1]