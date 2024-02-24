class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        tMap = {}
        sMap = {}
        #create tMap for String t my capturing character's count
        for i in range(0,len(t)):
            if t[i] in tMap:
                tMap[t[i]] = tMap[t[i]] + 1
            else:
                tMap[t[i]] = 1
        i=0
        count = 0
        #look for the first word in s which matches with any character in t
        while(i<len(s)):
            if s[i] in tMap:
                sMap[s[i]] = 1
                count =1
                break
            i+=1
        j=i+1
        if(len(t)==1 and s==t):
            return s
        minStr = s #intialize minStr with s
        result = ''
        while(j<len(s)):
#if we have character which exist in t but we have already take character into account => for example t=ba, s=bcba -> we should ignore second b and move j to next element
            if s[j] in sMap: 
                    if sMap[s[j]]>= tMap[s[j]]:
                        j+=1
                        continue
            if s[j] in tMap:
                    sMap[s[j]] = sMap[s[j]]+1 if s[j] in sMap else 1
                    count+=1
            if count== len(t) and len(minStr)>=j-i+1:
                    minStr = s[i:j+1]
                    result = minStr
                    print(minStr,len(minStr), j-i+1)
            if count==len(t) or j-i+1>len(t):
                if s[i] in sMap:
                    del sMap[s[i]]
                    i+=1
                    count-=1
                while i<len(s) and s[i] not in tMap:
                    i+=1
            j+=1
        return result       
