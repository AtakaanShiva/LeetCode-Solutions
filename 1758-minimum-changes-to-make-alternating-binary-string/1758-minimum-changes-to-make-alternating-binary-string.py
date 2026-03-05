class Solution(object):
    def minOperations(self, s):
     
        count0 = 0 
        
        for i in range(len(s)):
            
            if i % 2 == 0:
                if s[i] != '0':
                    count0 += 1
            else:
                if s[i] != '1':
                    count0 += 1
        
      
        count1 = len(s) - count0
        
        return min(count0, count1)