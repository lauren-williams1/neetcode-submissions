class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #heap

        #get frequency count for each number in the list
        # add each pair of count and number to the heap
        # iterate over heap to return top k elements


        map = {}
        for num in nums:
            map[num] = 1 + map.get(num,0)
        
        heap = []
        for num in map:
            heapq.heappush(heap, (map[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
