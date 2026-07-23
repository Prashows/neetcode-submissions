class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        liss = {}
        for data  in range(len(nums)):

            liss[nums[data]]= liss.get(nums[data], 0)+1
            if liss[nums[data]] > 1:
                return nums[data]
            