class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
   

        left =0 
        max_freq= 0
        maxlength =0

        elements={}

        for data in range(len(s)):

            right = s[data]
            elements[right] = elements.get(right,0)+1

            max_freq = max(max_freq, elements[right])

            while (-left + data +1) - max_freq > k:

                removingleft = s[left]
                elements[removingleft] -= 1
                left+= 1
            
            maxlength = max(maxlength , data - left +1)

        return maxlength
