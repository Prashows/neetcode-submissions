class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right  = res = max( piles)
        
        while left <= right:
            hours = 0
            mid = (left + right)//2
            for data in piles:
                
                if mid >= data:
                    hours += 1 
                else:
                    
                    hours += data // mid
                    if data %mid != 0:
                        hours += 1 
            
            if  hours > h :
                
                left = mid+1
            else:
                res = min(mid,res)
                right  =  mid -1

        return res
                
            

