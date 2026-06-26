class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        a=[]
        b=[]
        i=0
        for ch in s:
            a.append(ch)

        a.sort()
        print(a)
        
        for ch in t:
            b.append(ch)

        b.sort()
        print(b)
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
                break
            
        return True
                    