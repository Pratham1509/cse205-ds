class Solution(object):
    def removeStars(self, s):
        stack=[]
        i=0
        for i in range(len(s)):
            if s[i]!='*':
                stack.append(s[i])
            else:
                stack.pop()
        return ''.join(stack)
        