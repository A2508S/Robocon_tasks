class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        #taking R and L as x axis and U nd D as y axis. 
        x,y= 0,0
        for i in moves:
            if i == "R":
                x+=1
            elif i == "L":
                x-=1
            elif i =="U":
                y+=1
            else:
                y-=1
        return x == 0 and y==0
