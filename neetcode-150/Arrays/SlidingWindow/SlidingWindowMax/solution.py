class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        l=0
        r=0
        result = []
        while(r<len(nums)):
            #pop from right side till last element of queue is > current element
            while queue and nums[queue[-1]]<nums[r]:
                queue.pop()
            #append that index
            queue.append(r)
            #if index is out of bounce remove it from queue
            if l> queue[0]:
                queue.pop(0)
            #don't append in result until window length is achieved. append it after that
            if r + 1 >= k:
                result.append(nums[queue[0]])
                l+=1
            r+=1
        return result      
