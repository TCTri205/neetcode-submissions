class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            s.add(n)
        m = 0
        for e in s:
            if e-1 in s:
                continue
            length = 0
            tmp = e
            while tmp in s:
                tmp += 1
                length += 1
            m = max(length, m)
        return m