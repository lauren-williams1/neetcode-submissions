class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #create a frequency hashmap
        # each frequency, number pair to a heap
        # if heap is greater than k remove root value-smallest number from heap
        # iterate through the heap and grab the number from num, frequency pair and return it in list

        map = {}
        result = []

        for num in nums:
            map[num] = 1 + map.get(num, 0)

        heap = []
        for num in map:
            heapq.heappush(heap, [map[num], num])
            if len(heap) > k:
                heapq.heappop(heap)
        
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result




       


         