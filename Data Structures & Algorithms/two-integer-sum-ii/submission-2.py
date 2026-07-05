class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left=0
        right=len(numbers)-1
        d=[]
        for data in numbers:

            if numbers[left] + numbers[right] == target:
        
                d.append(left+1)
                d.append(right+1 )
                return d
                break
            elif numbers[left] +numbers[right] < target:
                left+=1
            else:
                right-=1