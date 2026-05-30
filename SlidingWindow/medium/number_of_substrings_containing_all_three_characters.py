from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i , j = 0 , 0 
        n = len(s)
        dict_ = defaultdict(int)
        res = (n+1) * n //2
        while j < n:
            dict_[s[j]] += 1
            while len(dict_) >= 3:
                dict_[s[i]] -= 1
                if dict_[s[i]] == 0:
                    del dict_[s[i]]
                i +=1
            res -= j - i + 1
            j += 1 
        return res


def main():
    test_cases = ["abcabc"  , "aaacb" , "abc"]

    for case in test_cases:
        print(Solution().numberOfSubstrings(case))


main()
