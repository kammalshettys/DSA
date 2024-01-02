"""
Approch 1
sort both strings
now compare both strings
if you don't find any match in between then return false

Time complexity
O(nlogn) => beacuse of sorting
Space Complexity
O(1)

Approach 2
    -create a hashmap
    -loop through characters of first string
        build your hashmap with key as character and value as count of character occurance 
        for example 
        str1 = aab
        map = a->2
            b->1

    -then loop through second string 
        -for each character find the key in hashmap and decrement the count value for that character
        -for example for string2 is "aba" after first itteration
            the map should be
            a->1
            b->1
        - if the key has count 0 then remove that character.
        - also if key doesn't exists then return false
    - after loop ends check the length of hashmap, if its zero then return true else false;

"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagDict = {}
        for i in range(0,len(s)):
            if s[i] in anagDict:
                anagDict[s[i]] = anagDict[s[i]]+1
            else:
                anagDict[s[i]] = 1
        for i in range(0,len(t)):
            if t[i] not in anagDict:
                return False
            else:
                anagDict[t[i]] = anagDict[t[i]] - 1
            if anagDict[t[i]]<=0:
                anagDict.pop(t[i])
        return len(anagDict)==0
        