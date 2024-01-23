"""
We will be using hashmaps for this problem.
Approach 1 -> this doesn't look like O(n)
run the loop for first time and store the element as key and element + 1 as value in hashmap
100->101
4->5
200->201
1->2
3->4
2->3

declare max_seq = 1
now loop through hashmap
for each key check its value exist as key of hashmap
1->2
for key 1, its value is 2, 
we will searching if 2 as key exists or not.
if exists we will run a loop 
and do the above until the above condition matches.
since we matched with 2
2->3
we will look for 3 
3->4
will look for 4
while doing this we will increment a local variable (count)
if count>max_seq then max_seq=count
return max_seq

Above approach gives time limit exceeded
Approach 2:
similar to approach 1 we will be using sets and store all the values in sets
we will again loop through nums
now we will make sequence with all the values in nums.
to find the start value of sequence we will look for left values of number.
if there is no left (element-1) value then we can consider that value as start of sequence.
in the above example.
100 can considered start of sequence as we dont have 99 value in list
similar 1 can consider start of sequence
2 is not considerent start of sequence because we have 1 in list.
once we have start of sequence value
we will try to make sequence by iterating recurisively with the value+1
and increment the count value if we are making any progress with sequence
for example 1 is start of sequence
we will look for 2,
we have 2 in set, then we look for 3 in set, then look for 4 so on...
after iteration store the longest seq value.
return longest_seq_value
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        conseq_set = {}
        if len(nums)==0:
            return 0
        for k in nums:
            conseq_set.add(k)
        max_req = 0
        for k in nums:
            if k-1 not in conseq_set:
                count=1
                while (k+1) in conseq_set:
                    count = count +1
                    k = k+1
                max_req = max(max_req,count)
        return max_req