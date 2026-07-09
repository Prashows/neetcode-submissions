class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack=[]
        newdata=0
        for data in tokens:

            
            if data == '+':
                newdata = int(stack[-2]) + int(stack[-1])
            elif data == '-':
                newdata = int(stack[-2]) - int(stack[-1])
            elif data =='*':
                newdata = int(stack[-2]) * int(stack[-1])
            elif data == '/':
                newdata = int(int(stack[-2]) / int(stack[-1]))
            else:
            
                stack.append(data)
                newdata= int(data)
                print(stack)
                continue
            stack.pop()
            stack.pop()    
            stack.append(newdata)
            


        return newdata
        