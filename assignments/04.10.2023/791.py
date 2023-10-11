class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        ans = []
        for i in order:
            if i in freq:
                ans.append(i*freq[i])
            freq[i] = 0
        for i in freq:
            if freq[i]!=0:
                ans.append(i*freq[i])
        return "".join(ans)