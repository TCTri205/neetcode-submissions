class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
            
        p = []
        for n, f in d.items():
            p.append([f,n])
        p.sort(reverse=True)

        res =[]
        for i in range(k):
            res.append(p[i][1])
        return res