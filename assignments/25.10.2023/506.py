class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        v = []
        ans = [''] * len(score)
        for i in range(len(score)):
            v.append((score[i], i))
        v.sort(reverse=True)
        for i in range(len(v)):
            if i == 0:
                ans[v[i][1]] = "Gold Medal"
            elif i == 1:
                ans[v[i][1]] = "Silver Medal"
            elif i == 2:
                ans[v[i][1]] = "Bronze Medal"
            else:
                ans[v[i][1]] = str(i + 1)
        return ans
        