"""
use hashmap
while creating dictionary
loop through each element
    - subtract each value with target
    - store the subtracted value as key and index as its corresponding value
    - before storing the value check if the element exits as key in hashmap

    [2,7,11,15]
    hashmap:
        7->0
        2->1
        -2->2
        -6->3

psuedo code:
    diffDictionary={}
    for i -> range(0,len(nums)):
        if nums[i] not in diffDictionary:
            value = target - nums[i]
            diffDictionary.add(value->i)
        else:
            return [i,diffDictionary.get(nums[i])]
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffDict = {}
        for i in range(0,len(nums)):
            if nums[i] not in diffDict:
                diff = target - nums[i]
                diffDict[diff] = i
            else:
                return [i,diffDict[nums[i]]]
        return [-1,-1]