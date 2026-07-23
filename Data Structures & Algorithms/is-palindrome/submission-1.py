class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = re.sub(r'\W+', '', s).lower()
        print(st)
        i, j = 0, len(st) - 1
        isPalindrome = True
        while i < j:
            if st[i] != st[j]:
                isPalindrome = False
                break
            i += 1
            j -= 1
        return isPalindrome