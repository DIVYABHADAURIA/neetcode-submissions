from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dc = Counter(s)

        if len(s) != len(t):
            return False
        
        for i in t: 
            if i not in dc or dc[i] == 0:
                return False 
            else:
                dc[i] -= 1
        return True

        

        