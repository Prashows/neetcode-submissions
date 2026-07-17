class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left =0
        right = 0
        from collections import deque

        dq =deque()
        output =[]

        while right < len(nums):

            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            if dq and dq[0] < left:
                dq.popleft()


            dq.append(right)

            if right +1 >=k:
                left+=1
                output.append(nums[dq[0]])
            right+=1
        return output