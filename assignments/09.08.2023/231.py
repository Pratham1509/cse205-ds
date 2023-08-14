class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<0:
            return False
        elif n==1:
            return True
        elif n%2==0:
            n=n/2
            return self.isPowerOfTwo(n)
        return False
