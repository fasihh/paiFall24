import heapq

class Solution:
    def smallestRange(self, nums):
        pq = []
        for i, elements in enumerate(nums):
            [heapq.heappush(pq, (element, i)) for element in elements]
        merged = [heapq.heappop(pq) for i in range(len(pq))]
        
        i, j = 0, 3
        interval = [float('-inf'), float('inf')]
        while j <= len(merged):
            lists = [False for __ in range(len(nums))]
            for k in range(i, j):
                lists[merged[k][1]] = True
            
            if not all(lists):
                continue

            a, b, c, d = interval[0], interval[1], merged[i][0], merged[j-1][0]
            if b - a < d - c or (a < c and b - a == d - c):
                interval = [c, d]

        return interval