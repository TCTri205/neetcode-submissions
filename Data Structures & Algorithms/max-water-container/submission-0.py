class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        res = -1
        while i < j:
            res = max(( (j-i) * min(heights[i], heights[j]) ), res)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return res