class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = {}
        for i in s:
            map[i] = map.get(i,0) + 1 

        

        for i in t:
            
            if i in map.keys() and map[i] != 0 :
             map[i] -= 1
            else:
                return False

        return True
               



        

        