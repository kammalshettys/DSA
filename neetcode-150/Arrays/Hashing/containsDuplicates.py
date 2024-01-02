"""
Approach
- create a new Set with array
- compare length of set and array.
- if the length are different then it means there are dublicates
- we are able to do this because set doesn't contains dublicates.

Psudo Code
    newSet = set(givenArray)
    if newSet.length != givenArray.Length => return true;
    else return false;

    Space Complexity = O(n)
    time Complexity = O(n)
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newSet = set(nums)
        return len(newSet)!=len(nums)