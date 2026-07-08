class Solution:
    def isValid(self, s: str) -> bool:
        


            
            stack=[]

            

            mapping ={ ')':'(' , '}':'{' ,']':'['}

            for data in s:

                if data in mapping:
                    top = stack.pop() if stack else '#'

                    if mapping[data] != top:

                        return False

                else:
                    stack.append(data)

            if len(stack) == 0 :
                return True
            else :
                return False