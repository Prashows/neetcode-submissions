class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        cars= sorted(zip(position,speed),reverse=True)
        result =[]

        for pos,sped in cars:

            time = (target -pos)/sped

            if  result and time <= result[-1]:
                continue

            result.append(time)

        return len(result)