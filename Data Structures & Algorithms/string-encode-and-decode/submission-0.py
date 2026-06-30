class Solution:

    def encode(self, strs: List[str]) -> str:
        encdata=""
        for data in strs:
            encdata += str(len(data)) +"#" + data
        
        return encdata

    def decode(self, s: str) -> List[str]:

        decoded = []
        i=0
        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1
            length= int(s[i:j])
            decoded.append(s[j+1:length +j +1])
            i= length + j +1
    
        return decoded





