from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        def atMost(k):
            i , j = 0 , 0 
            n = len(s)
            dict_ = defaultdict(int)
            res = 0
            while j < n:
                dict_[s[j]] += 1
                while len(dict_) > k:
                    dict_[s[i]] -= 1
                    if dict_[s[i]] == 0:
                        del dict_[s[i]]
                    i +=1
                res += j - i + 1
                j += 1
            return res

        return ((n+1) * n // 2) - atMost(2) # i have to understand why this worked


def main():
    test_cases = ["abcabc"  , "aaacb" , "abc"]

    for case in test_cases:
        print(Solution().numberOfSubstrings(case))


main()

