class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        seq_tree = {}
        result = []
        if k> len(nums):
            return []
        for i in range(0,k):
            seq_tree[i]= nums[i]
        seq_tree = self.getSortedWindow(seq_tree)
        result.append(self.getMaxVal(seq_tree))
        j=0
        #print(seq_tree,result)
        for i in range(k,len(nums)):
            del seq_tree[j]
            j +=1
            seq_tree[i]=nums[i]
            seq_tree = self.getSortedWindow(seq_tree)
            result.append(self.getMaxVal(seq_tree))
        # print(result)
        return result
            
    def getSortedWindow(self, seq_tree):
        sorted_tree = sorted(seq_tree.items(), key=lambda x:x[1],reverse=True)
        seq_tree = dict(sorted_tree)
        return seq_tree
    
    def getMaxVal(self, seq_tree):
        return seq_tree[list(seq_tree)[0]];
