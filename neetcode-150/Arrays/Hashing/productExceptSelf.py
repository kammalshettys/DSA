############################################################
# L0238.py
# Author: Sai Sumanth Kammal Shetty
###########################################################
############################################################
# All imports
###########################################################
from typing import List

############################################################
# You cannot change anything in Solution
###########################################################
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        work = [0]
        ans = []
        if (False):
            b = L0238(nums,ans,work,"Brute Force")
        if (False):
            b = L0238(nums,ans,work,"Use Division")
        if (False):
            b = L0238(nums,ans,work,"n time n space")
        if (True):
            b = L0238(nums,ans,work,"n time 1 space")
        return ans

############################################################
# You cannot change anything in L0238
###########################################################
class L0238:
    def __init__(self,a: List[int],ans: List[int], work:'list of size 1', alg:'string') -> None:
        self._a = a
        self._ans = ans
        self._work = work
        self._l = len(a)
        for i in range(self._l):
            self._ans.append(0) ## Data is allocated and initialized to 0
        Algorithm(self,alg)

    def __len__(self):
        return self._l;

    def getdata(self,i:'int')->'int':
        assert(i >= 0 and i < self._l)
        self._work[0] = self._work[0]+1 
        return self._a[i]

    def getans(self,i:'int')->'int':
        assert(i >= 0 and i < self._l)
        self._work[0] = self._work[0]+1 
        return self._ans[i]

    def setans(self,i:'int',v:'int')->'None':
        assert(i >= 0 and i < self._l)
        self._work[0] = self._work[0]+1 
        self._ans[i] = v 

class Algorithm:
    def __init__(self,s:'L0238', alg:'string') -> None: 
        self._s = s
        if (alg == "Brute Force"):
            self._nsquare_time_constant_space()
        elif (alg == "Use Division"):
            self._n_time_constant_space_with_divison()
        elif (alg == "n time n space"):
            self._n_time_n_space()
        elif (alg == "n time 1 space"):
            self._n_time_1_space()
        else:
            assert(False)

    ########################################
    # WRITE CODE BELOW
    #########################################
   
    ########################################
    # TIME:THETA(NSQUARE)
    # Space:THETA(1)
    #########################################
    
    def _nsquare_time_constant_space(self):
        n = len(self._s)
        for i in range(n):
            prod = 1
            for j in range(n):
                if(i!=j):
                    prod = prod*self._s.getdata(j)
            self._s.setans(i,prod)
        
                    

    ########################################
    # TIME:THETA(N)
    # Space:THETA(1)
    #########################################

    def _n_time_constant_space_with_divison(self)->'None':
        n = len(self._s)
        zeroCount = 0;
        #count number 
        for i in range(n):
            if(self._s.getdata(i)==0):
                zeroCount = zeroCount + 1
        if zeroCount > 1:
           for i in range(n):
               self._s.setans(i,0)
        else:
            totalProd = 1
            containsZero= False
            for i in range(n):
                if(self._s.getdata(i)==0):
                    containsZero= True
                else:
                    totalProd = totalProd*self._s.getdata(i)
            for i in range(n):
                if containsZero:
                    if self._s.getdata(i)==0:
                        self._s.setans(i,totalProd) 
                    else:
                        self._s.setans(i,0)
                else:
                    self._s.setans(i,totalProd//self._s.getdata(i))         
            

    ########################################
    # TIME:THETA(N)
    # Space:THETA(N)
    #########################################
    def _n_time_n_space(self)->'None':
        n = len(self._s)
        temp = []
        for i in range(n):
            if i==0:
                temp.append(1)
            else:
                temp.append(temp[i-1]*self._s.getdata(i-1))
        for i in range(n-1,-1,-1):
            if(i==n-1):
                self._s.setans(n-1,1)
            else:
                self._s.setans(i, self._s._ans[i+1]*self._s.getdata(i+1))
        for i in range(n):
            self._s.setans(i,self._s._ans[i]*temp[i])

    ########################################
    # TIME:THETA(N)
    # Space:THETA(1)
    #########################################
    def _n_time_1_space(self)->'None':
        n = len(self._s)
        temp = []
        for i in range(n):
            if i==0:
                self._s.setans(i,1)
            else:
                self._s.setans(i,self._s._ans[i-1]*self._s.getdata(i-1))
        r = 1;
        for i in range(n-1,-1,-1):
            if (i==n-1):
                r=1
            else:
                r = r*self._s.getdata(i+1)
            self._s.setans(i,self._s._ans[i]*r)
        