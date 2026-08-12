class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dc = defaultdict(list)
        
        for word in strs:
            lst = 26 * [0]
            for alpha in word:
                lst[ ord(alpha) - ord('a') ] += 1          
            dc[tuple(lst)].append(word)

            #if tuple(lst) in dc:
                #dc[tuple(lst)].append(word)
            #else:
                #dc[tuple(lst)] = [word]
        
        return [item for item in dc.values()]
            
        