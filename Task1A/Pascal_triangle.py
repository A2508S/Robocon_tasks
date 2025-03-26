class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tri = [[1]] #pascal triangle list
        for i in range(numRows-1):
            a = [1] #first element of row is 1, so started list with that
            b = tri[-1] + [0] #added 0 at last because the last element of a would have caused problems (below)
            for j in range(1,len(tri[-1])+1):
                a.append(b[j-1]+b[j]) 
            tri.append(a)
        return tri

            

        
