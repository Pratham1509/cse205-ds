class Solution(object):
    def generateParenthesis(self, n):
        result = []
        def gp(open,close,count,sr):
            if open==close==0:
                result.append(sr)
                return
            if open>0:
                gp(open-1,close,count+1,sr+'(')
            if close>0 and count>0:
                gp(open,close-1,count-1,sr+')')
        gp(n,n,0,"")
        return result