import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s_cleaned = "".join(char for char in s if char.isalnum())
        s_cleaned = re.sub(r'[^a-zA-Z0-9]', '', s)
        st = 0 
        ed = len(s_cleaned) - 1

        while st <= ed:
            if s_cleaned[st].lower() != s_cleaned[ed].lower():
                return False
            st += 1
            ed -= 1
        return True


        