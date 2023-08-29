class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        a=''.join(word1)
        b=''.join(word2)

        if a==b:
            return True
        else:
            return False
        