class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
            #In Python 2.7, the “/” operator works as a floor division for integer arguments.
                # >>> math.ceil(5/2)
                #2.0
                #>>> math.ceil(float(5)/2)
                #3.0
            #therefore, float(len(B)) is required
        min_length = int(math.ceil(float(len(B))/len(A)))
        for i in range(2):
            if B in (A * (min_length+i)):
                return min_length+i
        return -1
