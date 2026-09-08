class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxAr = 0

        stack =[] #pair (index and height)

        for i, h in enumerate(heights):
            start =i
            while stack and stack[-1][1] >h:
                index, height = stack.pop()
                maxAr = max(maxAr, height *(i-index))
                start = index
            stack.append((start,h))
        
        for i, h in stack:
            maxAr = max(maxAr, h*(len(heights)-i))
        
        return maxAr
