class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element={}
        value=[]
        for num  in nums:

            element[num]= element.get(num,0)+1
        
        sorted_items = sorted(element.items(), key = lambda x: x[1], reverse=True)
        
        
        result = [item[0] for item in sorted_items[:k]]

        return result

        