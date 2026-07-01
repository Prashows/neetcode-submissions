class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

            output=[1]*len(nums)
            length = len(nums)

            left=1
            right=1


            for i in range(length):

                output[i] = left
                
                left *= nums[i]

            for i in range(length-1,-1,-1):

                output[i] *= right 
                right *= nums[i]

            return output
            