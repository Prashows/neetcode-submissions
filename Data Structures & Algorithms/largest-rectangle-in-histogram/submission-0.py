class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea =0
        stack=[]
        prev =0
        for i,hei in enumerate(heights):

            newindex= i
            while stack and stack[-1][-1] > hei:

                index, data =    stack.pop()

                area = data * ( i- index)
                maxarea = max(area,maxarea)
                newindex = index
            stack.append((newindex,hei))

        for i,data in stack:

            maxarea =  max(maxarea, data * (len(heights)-i))

        return maxarea