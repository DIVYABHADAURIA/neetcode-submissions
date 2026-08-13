class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = []

        for item in strs:
            res.append(str(len(item)) + "#")
            res.append(item)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        i = 0 
        res = []
        #print(s)
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            #print(i,j)
            length = int(s[i:j])

            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res