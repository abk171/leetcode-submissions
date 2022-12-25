class Solution(object):
    def psum(self, prev, n):
        return prev + 12 * n ** 2
    
    def minimumPerimeter(self, neededApples):
        """
        :type neededApples: int
        :rtype: int
        """
        p = 0
        n = 0
        while(neededApples > p):
            
            n += 1
            p = self.psum(p, n)
            
        return 8 * n
        