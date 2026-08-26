class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        l = height[i]
        r = height[j]
        res = 0
        while i < j:
            if l < r:
                i += 1
                if l < height[i]:
                    l = height[i]
                else:
                    res += l - height[i]
            else:
                j -= 1
                if r < height[j]:
                    r = height[j]
                else:
                    res += r - height[j]
        return res
