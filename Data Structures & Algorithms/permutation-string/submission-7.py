class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
                
     
        chars={}
        for data in s1:
            chars[data] = chars.get(data,0)+1
            


        left =0
        have =0
        need = len(chars)
        maxstring= len(s1)
        window ={}
        for right in range(len(s2)):
            newdata = s2[right]
            
            window[newdata] = window.get(newdata,0)+1
        
            if newdata in chars and window[newdata] == chars[newdata]:
                have += 1
            while (right -left +1) > maxstring:

                popdata = s2[left]
                window[popdata] -=1
                
                

                if popdata in chars  and window[popdata] == chars[popdata]-1:
                    have -= 1
                
                
                left+=1
            if have == need:
                return True
        return False
        
        
 
        


        