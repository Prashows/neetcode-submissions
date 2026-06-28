class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        newlist={}

        for ch in strs:

            sdata= "".join(sorted(ch))

            if sdata not in newlist:
                newlist[sdata]=[]
    
            newlist[sdata].append(ch)

        return list(newlist.values())