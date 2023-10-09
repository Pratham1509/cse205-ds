class Solution(object):
    def backspaceCompare(self, s, t):
        stack1=[]
        stack2=[]
        i,j=0,0
        for i in range(len(s)):
            if s[i]!='#':
                stack1.append(s[i])
            else:
                stack1.pop()
        for j in range(len(t)):
            if t[j]!='#':
                stack2.append(t[j])
            else:
                stack2.pop()
        return stack1==stack2
        