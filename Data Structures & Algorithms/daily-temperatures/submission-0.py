class Solution:
    def dailyTemperatures(self, temp : List[int]) -> List[int]:
        stack= []
        result =[0]* len(temp)
        left= 0

        for i,data  in  enumerate(temp):

            
            while stack and     data  > temp[stack[-1]]:

                top = stack[-1]
                stack.pop()
                result[top] =  i - top
            
                
            stack.append(i)    
        return result