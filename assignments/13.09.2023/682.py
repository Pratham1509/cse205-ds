class Solution(object):
    def calPoints(self, operations):
        res=[]
        for i in operations:
            if i=='C':
                res.pop()
            elif i=='D':
                res.append(res[-1]*2)
            elif i=='+':
                sm=res[-1]+res[-2]
                res.append(sm)
            else:
                res.append(int(i))
        # print(res)
        return sum(res)
        