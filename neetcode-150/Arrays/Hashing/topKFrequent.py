"""
bucket sort is what we will be using here
- use hashmap for tracking the number occurrance and key should be the elment in the loop and value should be its occurance
bucket insertion
- create a array of input array length
- the element in array is also array, [[1,2,3],[5,6]]
    - we have hash map with keys as distinct elements of input array and values as occurance count.
    - loop through hashmap
    - below is the idea behind bucket sort.
    - as we know  the count(occurance) of elements which is stored in values of hashmap doesn't exceed length of array. Thus we can store the elements (key of hashmap) against the index of array.
    - here we will using values of hashmap as index of arrays.
    - if we have two same values for two different elements we will be using array to store that element.
    -example 
    input arr= [1,1,1,2,2,3]
    hash map = {
        1->3
        2->2
        3->1
    }
    bucket created = [null,[3],[2],[1],null,null]
- to get the result set iterate through the bucket in reverse order
- ignore null elements, append the non null values in result set untill resultset length==k



"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}
        for num in nums:
            if num in countDict:
                countDict[num] = countDict[num]+1
            else:
                countDict[num] = 1
        arr = [None]*(len(nums)+1)
        
        for r,v in countDict.items():
            innerArr = []
           # print(k,v)
            if arr[v] is None:
                innerArr.append(r)
            else:
                innerArr= arr[v]
                innerArr.append(r)
            arr[v]=innerArr
        resultset = []
        print("k",k)
        count=k
        i = len(arr)-1
        while count>0:
            a = arr[i]
            print(a,i,count,k)
            if a is not None:
                for ele in a:
                    resultset.append(ele)
                    count = count-1
            i = i-1
        return resultset
        