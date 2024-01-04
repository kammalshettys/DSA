"""
 Approach 1:
 declare hashMap
 here hashMap would of type <string,List>
 loop through array
    st = sorted string (eat becomes aet)
    check if st exists in hashmap
    if yes 
        get list of st key from hashmap
        push the element in list
        update hashmap for st key with the updated array
    else 
        create new array
        push element in list
        update hashmap with st, new array 
loop through hashmap
    push arrays of hashmap in result list
return result

time complexity: O(nmlogm)
    m= average size of string
    n = size of arrays
space complexity:
    n2 -> saving the data in resultset

 Approach 2:
 sorting in approach 1 increases time complexity 
 to resolve that we will write a method which takes string as input and returns a string 
    intialize of array of size 26 with zeros
    loop through string
        arrIndex= get ascii value of character
        increment the value of arr[arrIndex] with 1
    join the array values into string with some divider like ":"   
  now use the resultant string as key for hashmap and rest of the code remains same
  Earlier sorting took mlogm timecomplexity and now it takes O(m) time complexity for creating key
  resulting the code complexity to O(mn)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angDict = {}
        for s in strs:
            key = self.generateKey(s)
            arr = []
            if key not in angDict:
                arr.append(s)
            else:
                arr = angDict[key]
                arr.append(s)
            angDict[key]= arr
        resultSet = []
        for k,v in angDict.items():
            resultSet.append(v)
        return resultSet
    def generateKey(self, s):
        arr = [0]*26
        for c in s:
            index = ord('a') - ord(c)
            arr[index] = arr[index] + 1
        return "".join(str(arr))

        