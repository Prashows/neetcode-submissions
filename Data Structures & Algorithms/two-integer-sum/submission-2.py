class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[]
        for i,num in enumerate(nums):
            arr.append((num,i))
        
        arr.sort()
        left=0
        right=len(arr)-1
        while left < right:

            total = arr[left][0]+arr[right][0]
            if total == target:
                return sorted([arr[left][1],arr[right][1]])
            elif total< target:
                left +=1
            else:
                right -= 1