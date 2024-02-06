class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = 1
        sub_dict = {}
        maxSubLength = 0
        j = 0
        for i in range(0,len(s)):
            if s[i] in sub_dict:
                sub_dict[s[i]] = sub_dict[s[i]] + 1
                maxFreq = max(maxFreq, sub_dict[s[i]])
            else:
                sub_dict[s[i]] = 1
            k1 = (i-j+1) - maxFreq
            if k1>k:
                sub_dict[s[j]] = sub_dict[s[j]] - 1
                j +=1
            print(i,j)
            maxSubLength = max(maxSubLength, i-j+1)
        return maxSubLength

            
            
        