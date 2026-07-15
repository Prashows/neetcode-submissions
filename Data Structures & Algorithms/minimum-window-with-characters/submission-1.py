class Solution:
    def minWindow(self, s: str, t: str) -> str:
           
        countt={}
        for data in t:
            countt[data] = countt.get(data,0)+1

        left =0 
        window ={}
        have =0
        need = len(countt)
        result =[-1,-1]
        resultlen = float("infinity")

        if not s or not t:
            return ""


        for right in range(len(s)):

            char = s[right ]

            window[char]= window.get(char , 0)+1

            if  char in countt and window[char]== countt[char]:
                have +=1 


            while need == have:

                if (right- left +1 ) < resultlen:

                    result =[left ,right]

                    resultlen = right -left +1
                
                left_char =s[left]
                window[left_char] -= 1

                if left_char in countt and window[left_char]< countt[left_char]:
                    have-=1
                
                left +=1

        return s[result[0]: result[1] +1 ] if resultlen != float('infinity') else ""    