class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # create a dict to get frequency count for each unique number in array
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1

        
        # create a heap, add each pair to the heap
        # if len of the heap is > k, pop heap
        heap = []
        for num in map:
            heapq.heappush(heap, (map[num], num))
            if len(heap) > k:
                heapq.heappop(heap)



        # iterate over heap and grab unique numbers that are top k elements
        # return that in indices
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
        