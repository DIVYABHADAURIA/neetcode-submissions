class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for i in strs:
            ls =  [0] * 26
            for j in i:
                ls[ord(j) -  ord('a')] += 1
            map[tuple(ls)].append(i)


        return list(map.values())

        


        

        