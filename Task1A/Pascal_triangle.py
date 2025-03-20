class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tri = [[1]]
        for i in range(numRows-1):
            a = [1]
            b = tri[-1] + [0]
            for j in range(1,len(tri[-1])+1):
                a.append(b[j-1]+b[j])
            tri.append(a)
        return tri

            

        
