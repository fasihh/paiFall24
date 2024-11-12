class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0] * 26
        for c in s1:
            freq[ord(c) - ord('a')] += 1
        
        for i, j in enumerate(range(len(s1)-1, len(s2))):
            curr_freq = [0] * 26
            for k in range(i, j+1):
                curr_freq[ord(s2[k]) - ord('a')] += 1
            if curr_freq == freq:
                return True
        return False



s1 = "ab"
s2 = "eidbaooo"

print(Solution().checkInclusion(s1, s2))